---
date: 2026-06-08
source: chatgpt
title: "Event Bus Refactor"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Added a synchronous in-process event bus and moved the trading execution path onto it.

  New files:

  - kalshi-watch/events.py - subscribe(), publish(), clear_listeners()
  - kalshi-watch/trading/listeners.py - records and Telegram listeners
  - kalshi-watch/test_events.py
  - kalshi-watch/test_trading_events.py

  trading.runner.execute_signal() now publishes:

  - trade_rejected
  - trade_blocked
  - trade_submitted
  - trade_failed

  Listeners now handle:

  - persistence via save_recommendation
  - Telegram notification for submitted/failed trades

  This keeps execution deterministic and synchronous for now, but separates workflow from side effects so analytics can
  later subscribe without changing execution logic.

  Verification:

  python3 -m compileall events.py trading test_events.py test_trading_events.py
  ./venv/bin/python -m unittest test_events.py test_trading_events.py
  ./venv/bin/python -m unittest discover -p 'test_*.py'

  Full unittest discovery: 101 tests passed.

**ChatGPT:** That’s a strong refactor.

Best part: **execution is now the source of truth**, and persistence/Telegram are just subscribers. That is exactly the right shape before adding:

- analytics attribution listeners
- live-vs-demo listeners
- audit/event log listeners
- Polymarket read-only signal listeners
- Telegram manual trade command listeners

One thing I’d check next: make sure listener failures **cannot break order execution** unless you intentionally want that. For example, Telegram failing should not make `execute_signal()` look like trade execution failed.

Ideal rule:

- order submit fails → `trade_failed`
- risk blocks → `trade_blocked`
- DB save fails → logged as side-effect error, not execution failure
- Telegram fails → logged only

Also, I’d strongly consider adding a raw `trade_events` table soon. Even if `save_recommendation` already persists recommendations, an append-only event log will make analytics/debugging way easier.
