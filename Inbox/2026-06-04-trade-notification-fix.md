---
date: 2026-06-04
source: chatgpt
title: "Trade Notification Fix"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Short answer: not tons of live resting orders, but yes, the bot is producing a lot of attempted/rejected trade records and Telegram “Demo Trade Placed” alerts that are misleading.

I checked the local DB and live demo positions:

What’s actually live
- Live nonzero demo positions: 4
- Resting orders on those positions: 0
- The Iran nuclear deal ticker you sent: flat, no resting orders.
- So it is not building a huge pile of never-filling live orders.

What it is doing
- In the recent window I checked, there were:
  - 68 failed BUY_DEMO_YES attempts
  - 7 filled_or_submitted attempts
  - 0 currently resting orders in synced demo positions
  - 12,352 NO_TRADE risk failures logged locally

The bad part: hermes_bridge.py calls notify_after_trade(trade) even when status = "failed", and the notification template always says “Demo Trade Placed”. So failed duplicate-position checks are being announced as if they were trades.

My read
- The exchange/bot guard is preventing many of these from actually becoming orders.
- The bot is noisy and probably over-evaluating/retrying candidates.
- The notification wording is wrong and making it look scarier than the live account state.
- There may also be a stale/local duplicate-position guard issue, since the Iran ticker was flat live but got Duplicate position check failed.

Best next fix: change the notifier so failed/rejected attempts say “Demo Trade Failed” and only “Placed” for filled_or_submitted / filled, then inspect the duplicate-position guard.

**ChatGPT:** Yes — that read is solid.

I’d fix in this order:

1. **Stop misleading alerts first**
   - `failed` → “Demo Trade Failed”
   - `rejected/no_trade` → “Demo Trade Rejected”
   - only `filled`, `submitted`, `filled_or_submitted` → “Demo Trade Placed”

2. **Only count real attempts as trades**
   - Failed duplicate checks should not increment trade stats/cooldowns the same way as placed orders.

3. **Inspect duplicate-position guard**
   - It may be checking stale local rows instead of live synced positions.
   - Flat live ticker + duplicate failure means local DB state is probably dirty or not being reconciled correctly.

Best patch idea:

```python
def notification_title_for_trade(trade):
    status = (trade.get("status") or "").lower()

    if status in {"filled", "submitted", "filled_or_submitted"}:
        return "📊 Demo Trade Placed"

    if status in {"failed", "error"}:
        return "⚠️ Demo Trade Failed"

    if status in {"rejected", "no_trade", "blocked"}:
        return "🚫 Demo Trade Rejected"

    return "ℹ️ Demo Trade Attempt"
```

Then in `notify_after_trade(trade)`, replace the hardcoded title with:

```python
title = notification_title_for_trade(trade)
```

Also add the actual status near the top of the alert:

```python
Status: {trade.get("status", "unknown")}
```

The next real bug to chase is:

```text
Duplicate position check failed
```

when Kalshi live/demo says the ticker is flat. That means the bot’s local “open position” source is not trustworthy enough yet.
