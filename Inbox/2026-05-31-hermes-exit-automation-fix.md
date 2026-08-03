---
date: 2026-05-31
source: chatgpt
title: "Hermes Exit Automation Fix"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** • Fixed the exit automation path.

  Root cause: hermes_position_monitor.py assumed every open holding was a long Yes position. No positions had
  position_fp = -1, so Hermes kept skipping exits with messages like:

  live demo position is not long YES (-1)

  I changed the monitor to:

  - read open positions from live demo_market_positions, not reconstructed BUY_DEMO_YES rows
  - derive the held side from position_fp
      - position_fp > 0 => Yes
      - position_fp < 0 => No

  - evaluate No positions using derived No bid/ask
      - no_bid = 100 - yes_ask
      - no_ask = 100 - yes_bid

  - submit the correct exit action:
      - Yes holding => SELL_DEMO_YES
      - No holding => SELL_DEMO_NO

  - allow high-price demo exits up to 99¢ instead of blocking exits above 95¢

  Changed:

  - kalshi-watch/hermes_position_monitor.py:250
  - kalshi-watch/demo_trader.py:19

  Important: during validation, the monitor did execute live demo exits because config.demo.env has
  ENABLE_DEMO_EXIT_ORDERS=true.

  Recorded results:

  - KXHORMUZNORM-26MAR17-B260801 exited via SELL_DEMO_NO at 61¢, status filled
  - KXUSAIRANAGREEMENT-27 exited via SELL_DEMO_YES at 54¢, status filled
  - KXSAVEACT-27-JAN04 submitted SELL_DEMO_NO at 91¢, status resting
  - KXHORMUZNORM-26MAR17-B260615 was previously blocked at 96¢; that guard is now fixed, so the next monitor run can
    submit it

  Validation:

  - py_compile passes for hermes_position_monitor.py and demo_trader.py
  - Dry-run decision check now shows Jun 15 Hormuz No would exit at 96¢
  - Could not run pytest because this venv does not have pytest installed.

─ Worked for 6m 50s ─────────────────────────────────────────────────────────────

**ChatGPT:** This is a **major fix**. Hermes was not really “exit-capable” before because it treated No positions incorrectly.

What it means:

**Before:**  
Hermes could detect a bad position, but if it was actually a **No holding**, it thought: “this is not long Yes, skip exit.”  
So the sell alert was informational, not reliably executable.

**Now:**  
Hermes knows:

- Positive `position_fp` = holding **Yes**
- Negative `position_fp` = holding **No**
- Yes exits use `SELL_DEMO_YES`
- No exits use `SELL_DEMO_NO`

The most important validation is this:

- `KXHORMUZNORM...` exited No at **61¢ filled**
- `KXUSAIRANAGREEMENT-27` exited Yes at **54¢ filled**

So yes — it is now actually exiting demo positions.

The one concern:  
`KXSAVEACT` is **resting** at 91¢, meaning the exit was submitted but not filled yet. That is normal if there was not enough immediate opposing liquidity. Hermes should now track whether resting exits get filled, stale, canceled, or repriced.

Next thing I would add is an **exit order lifecycle monitor**:

> submitted exit → resting → filled / stale → cancel-replace lower/higher → final exit state

Because now the exit path works, but Hermes still needs to manage exits after submission, not just fire once and assume it is done.

**You:** • Yes. The exit-order lifecycle limit is STALE_EXIT_ORDER_MINUTES, defaulting to 5 minutes in kalshi-watch/
  hermes_position_monitor.py:62.

  Behavior:

  - Hermes allows one submitted exit order per ticker + exit action.
  - If an exit order is younger than 5 minutes, Hermes leaves it alone.
  - After 5 minutes, Hermes refreshes the Kalshi order status.
  - If filled, it marks the local trade as filled.
  - If canceled/closed, it places a replacement.
  - If still resting after 5 minutes, Hermes tries to cancel it, then places a replacement if cancellation succeeds.

  Current submitted exit orders in the local DB:

  KXHORMUZNORM-26MAR17-B260615  SELL_DEMO_NO   96¢  submitted
  KXSAVEACT-27-JAN04            SELL_DEMO_NO   91¢  submitted

  There is also an old stale KXAAAGASM submitted row, but since that is not a current live position it should not block
  current exits.

  There is no retry-count cap right now, only the time-based stale lifecycle. If you want a hard limit like “cancel
  after 3 replacement attempts” or “never chase an exit longer than 30 minutes,” that does not currently exist.

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────

**ChatGPT:** That is good — Hermes **does have basic exit-order lifecycle management now**.

The main missing piece is a **safety ceiling**.

Right now it can do this forever:

> submit exit → wait 5 min → cancel → replace → wait 5 min → cancel → replace

That is okay for demo, but I would add two limits:

1. **Max replacement attempts**
   - Example: `MAX_EXIT_REPLACEMENTS=3`
   - After 3 failed replacements, mark as `EXIT_STUCK`

2. **Max total exit chase time**
   - Example: `MAX_EXIT_CHASE_MINUTES=30`
   - After 30 minutes, stop blindly replacing and send a Telegram alert:
   - “Manual review needed — exit order stuck.”

For your bot, I’d do:

```env
STALE_EXIT_ORDER_MINUTES=5
MAX_EXIT_REPLACEMENTS=3
MAX_EXIT_CHASE_MINUTES=30
```

And the lifecycle should become:

```text
open position
→ exit signal
→ submit exit
→ resting
→ after 5 min refresh
→ if filled: done
→ if canceled/closed: replace
→ if still resting: cancel + replace
→ after 3 replacements or 30 min: EXIT_STUCK + alert
```

The old `KXAAAGASM` row not blocking exits is also correct behavior. The live position table should be the source of truth, not old local submitted rows.
