---
date: 2026-05-25
source: chatgpt
title: "Max Order Size Explanation"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** What is max order size

**ChatGPT:** In the context of urlKalshihttps://kalshi.com or trading systems generally, **max order size** means the **largest single trade/order you’re allowed to place at once**.

That limit can be determined by:
- the exchange/platform
- your account permissions
- market liquidity
- risk controls in your bot
- available counterparties in the order book

For example:
- If a market has very thin liquidity, your bot might cap orders at **$5–$25** to avoid moving the market.
- A platform itself might limit you to a certain number of contracts per order.
- Your own trading logic may intentionally enforce:
  - `max_order_size = 10`
  - meaning no trade larger than 10 contracts executes.

In your Kalshi bot setup, you’ll usually want **your own max order size setting** even if Kalshi allows more. That protects against:
- bad signals
- liquidity traps
- runaway automation
- accidental oversized positions

For a low-frequency demo test like you mentioned earlier, a reasonable starting point is:
- **1–5 contracts per trade**
- or
- **$1–$10 notional risk per position**

Example:
```python
MAX_ORDER_SIZE = 3
```

Then before placing an order:
```python
size = min(calculated_size, MAX_ORDER_SIZE)
```

That way your strategy can never exceed your risk cap even if the signal spikes.

**You:** simpler

**ChatGPT:** Max order size = the biggest trade you can place at one time.

Example:
- Max order size = 5
- Your bot can only buy/sell up to 5 contracts in a single order.

It’s basically a safety limit to stop trades from being too large.

**You:** • Yes. Hermes is now actively monitoring and attempting demo execution.

  What changed:

  - Added hermes-demo-trader.service
  - Added hermes-demo-trader.timer
  - Enabled the timer under your user systemd
  - It runs every 1 minute:

    hermes_bridge.py demo_execute --limit 1 --lookback-minutes 15

  Current status:

  - Timer is active and waiting for the next run.
  - It already fired successfully.
  - Latest run found a signal, but did not trade because it failed risk:

    status: failed_risk
    reason: liquidity too low
    size: 10

  So the active flow is now:

  Kalshi Watch signals
  → Hermes demo_execute
  → risk rules
  → frequency rules
  → Kalshi DEMO order if allowed
  → DB row
  → Telegram for submitted/rejected/failed order attempts

  It is still demo-only. To stop it:

  systemctl --user disable --now hermes-demo-trader.timer

**ChatGPT:** That means your system is now live in a controlled demo-trading loop.

Right now the flow is:

1. Your watcher detects a possible trade signal  
2. Hermes checks:
   - liquidity
   - risk limits
   - timing/frequency
3. If it passes:
   - a demo Kalshi order is placed
   - Telegram gets notified
   - trade is logged
4. If it fails:
   - it logs the rejection reason instead

The important part here is:

> “liquidity too low”

That means the bot is working correctly — it saw a trade opportunity, but your safety rules blocked it.

So:
- ✅ Signals are working
- ✅ Hermes is running automatically every minute
- ✅ Risk management is active
- ✅ Demo execution path is connected
- ❌ No actual demo trade has passed filters yet

Your setup is now at the “paper trading / dry-run validation” stage before real money.
