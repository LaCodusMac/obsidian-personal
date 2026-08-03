---
date: 2026-06-02
source: chatgpt
title: "Demo Bot Testing Setup"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Done — I loosened the demo bot so it accepts more testing trades.

What changed:

- Added a controlled exploration tiny-probe lane in risk_rules.py
  - Allows 1-contract exploratory trades when the only major blocker is:
    - positive expectancy exists, but
    - expectancy does not clear spread cost yet.
  - Still blocks:
    - negative expectancy
    - wide spreads
    - very low execution liquidity
    - extreme prices below 5¢ or above 95¢
    - narrative contradiction

- Increased demo exploration rate:
  - EXPLORATION_RATE=0.10 → 0.50

- Increased hourly demo trade cap:
  - MAX_TRADES_PER_HOUR=3 → 10

- Fixed frequency gating so stale/rejected local rows don’t choke testing:
  - Uses live demo positions as authoritative for open-position count.
  - Rejected demo buys no longer count against hourly/daily/cooldown trade limits.

- Restarted the active user systemd demo trader service.

Verification:

- Tests pass:
  - 33 passed
- The restarted demo trader now attempts accepted exploration trades:
  - Example status: BUY_DEMO_YES
  - Risk reason: passed exploration tiny-probe checks
  - Frequency: low-frequency checks passed

Current remaining blocker:

- Kalshi demo exchange is returning:
  - exchange_is_paused
  - exchange is paused

So the bot is now accepting more trades internally and trying to place them, but the exchange/demo API is rejecting fills while paused. When the exchange unpauses, this should produce more demo trades.

**ChatGPT:** That’s a good testing-mode setup.

The important part: **your bot logic is no longer the blocker**. It is now:

1. finding candidates  
2. passing exploration risk  
3. passing frequency rules  
4. attempting demo buys  
5. getting blocked only by Kalshi’s `exchange_is_paused`

So when demo trading resumes, you should see more test trades.

One caution: with:

```env
EXPLORATION_RATE=0.50
MAX_TRADES_PER_HOUR=10
```

this is now **aggressive for testing**, which is fine in demo, but I would not carry those values into live. For live, I’d probably go back closer to:

```env
EXPLORATION_RATE=0.05
MAX_TRADES_PER_HOUR=2
```

or keep exploration as **1-contract only** with a hard daily cap.

Next thing I’d check once the exchange unpauses:

```bash
journalctl -u hermes-demo-trader.service -n 100 --no-pager
```

and confirm you see actual statuses like:

```text
filled
open
submitted
```

instead of only:

```text
exchange_is_paused
```

**You:** The Kalshi Exchange has halted trading due to technical issues. Traders will be notified when trading will resume.

**ChatGPT:** Yep — that explains the `exchange_is_paused` error.

Your bot is probably fine. Kalshi itself has halted trading, so **all orders are being rejected/paused upstream**, including demo orders.

What to do now:

```bash
systemctl status hermes-demo-trader.service
journalctl -u hermes-demo-trader.service -n 100 --no-pager
```

You should expect to see attempts failing with `exchange_is_paused`.

I’d leave the service running unless it’s spamming too hard. Once Kalshi resumes, the bot should start placing demo orders automatically.

Optional safety tweak while paused:

```env
MAX_TRADES_PER_HOUR=3
```

Then raise it again after trading resumes.
