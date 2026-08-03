---
date: 2026-06-08
source: chatgpt
title: "Hermes Bridge Refactor"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** 3. Hermes bridge is becoming a god object

hermes_bridge.py

is now:

CLI
signal retrieval
execution
database writes
notifications

This is manageable today but will become painful when you add:

live trading
manual Telegram orders
Polymarket feeds

**ChatGPT:** Yes — that critique is right.

`hermes_bridge.py` should become a thin orchestration layer, not the place where every bot behavior lives.

I’d split it like this:

```text
kalshi-watch/
├── hermes_bridge.py              # CLI entry point only
├── trading/
│   ├── runner.py                 # demo_execute / live_execute orchestration
│   ├── signals.py                # get candidates/signals
│   ├── execution.py              # place/cancel/submit orders
│   ├── sizing.py                 # dollar sizing, lane sizing
│   ├── records.py                # trade DB writes
│   ├── notifications.py          # Telegram/alert formatting
│   └── manual.py                 # future Telegram manual order handling
├── venues/
│   ├── kalshi.py                 # Kalshi client wrapper
│   └── polymarket.py             # future read-only feed wrapper
```

Best next refactor:

```text
hermes_bridge.py
```

should only do:

```python
def main():
    args = parse_args()
    run_command(args)
```

Then move the current `demo_execute` logic into:

```python
trading/runner.py
```

Something like:

```python
def run_demo_execute(limit: int, lookback_minutes: int) -> None:
    signals = load_trade_candidates(limit, lookback_minutes)

    for signal in signals:
        decision = evaluate_signal(signal)

        if not decision.should_trade:
            persist_rejection(signal, decision)
            continue

        order = build_order(signal, decision)
        result = execute_demo_order(order)

        persist_trade(signal, decision, result)

        if result.submitted:
            notify_trade_placed(signal, decision, result)
        else:
            notify_trade_failed(signal, decision, result)
```

The big rule I’d follow:

**Bridge parses commands. Runner coordinates workflow. Execution places orders. Records writes DB. Notifications talk to Telegram.**

That will make live trading, Telegram manual orders, and Polymarket feeds much easier to add without turning `hermes_bridge.py` into a 2,000-line risk surface.
