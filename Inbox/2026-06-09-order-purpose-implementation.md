---
date: 2026-06-09
source: chatgpt
title: "Order Purpose Implementation"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** One important note: this patch centralizes the purpose model and uses it in the active dedupe logic already added, but
  it does not yet propagate REBALANCE through any live strategy path because there is no rebalance flow in the current
  codebase. If you want, I can do the next pass to thread order_purpose explicitly through every call site and record
  schema touchpoint, even where the current defaults already cover behavior.

**ChatGPT:** Yes — do the next pass.

That note is basically saying: **the model exists, dedupe is using it, but the rest of the system still treats purpose as implicit/defaulted.** That is fine as an intermediate patch, but I would not leave it there long-term.

What I would ask for next:

```text
Thread order_purpose explicitly through every trade/order path, even where the default is currently ENTRY.

Goal:
Make ENTRY / EXIT / REBALANCE / MANUAL / PROBE first-class everywhere so dedupe, records, notifications, analytics, and future rebalance logic all agree on why an order exists.

Scope:
1. Add order_purpose to all signal/order/trade DTOs or dicts.
2. Pass order_purpose through execute_signal, demo_execute, manual trade handlers, Telegram commands, and position monitor exits.
3. Persist order_purpose in the trade/recommendation/order records schema.
4. Include order_purpose in Telegram notifications and explainability output.
5. Update active dedupe to use purpose intentionally:
   - ENTRY should dedupe against existing ENTRY exposure.
   - EXIT should dedupe against active EXIT orders for the same position.
   - REBALANCE should be allowed to coexist with ENTRY/EXIT only where explicitly intended.
   - PROBE/exploration should be separately visible.
6. Add tests proving ENTRY, EXIT, MANUAL, PROBE, and REBALANCE dedupe behavior.
7. Keep backward-compatible defaults as ENTRY only at external boundaries, not deep inside business logic.

Important:
Do not add fake rebalance behavior yet. Only make the plumbing explicit so a future rebalance strategy can use it cleanly.
```

My read: **centralizing the purpose model was the right first move.** But if you stop there, you risk having a “pretend architecture” where the enum exists but behavior still depends on hidden defaults. For Hermes, that is exactly the kind of thing that later causes duplicate orders, noisy Telegram alerts, or analytics buckets that lie.

The best target state is:

```text
Signal says what it wants.
Risk validates whether that purpose is allowed.
Execution submits that purpose.
Records persist that purpose.
Notifications explain that purpose.
Dedupe uses that purpose.
Analytics learns from that purpose.
```

I would also explicitly tell it **not** to overbuild REBALANCE yet. Just make it impossible for future rebalance code to be ambiguous.

**You:** what should i do now

**ChatGPT:** Do **one focused patch now**: thread `order_purpose` everywhere, but **do not build rebalance behavior yet**.

Use this as your next instruction:

```text
Do the next pass to make order_purpose explicit across the system.

Do not implement a rebalance strategy yet.

Goal:
Every order, trade, recommendation, notification, and record should know its purpose:
ENTRY, EXIT, MANUAL, PROBE, REBALANCE.

Required changes:
1. Add order_purpose to the core trade/order data structures.
2. Thread it through:
   - execute_signal
   - demo_execute
   - manual Telegram trade handlers
   - position monitor exit orders
   - records/save_recommendation
   - Telegram notifications
3. Persist it in the database where trade/recommendation/order records are stored.
4. Include it in trade explainability output and position watch notifications.
5. Update active dedupe to use order_purpose consistently.
6. Add tests for:
   - ENTRY does not duplicate ENTRY
   - EXIT does not duplicate EXIT
   - MANUAL is visible as MANUAL
   - PROBE/exploration is visible as PROBE
   - REBALANCE is accepted as a purpose but does not trigger any rebalance logic yet

Keep backwards compatibility:
If older code does not provide order_purpose, default to ENTRY only at the system boundary.
Do not hide defaults deep inside execution or records logic.
```

After that patch, run:

```bash
cd /home/carlthellama/kalshi-watch

python3 -m compileall .
./venv/bin/python -m unittest discover -p 'test_*.py'
```

Then check what files changed:

```bash
git status
git diff --stat
```

What I would **not** do yet:

```text
Do not add rebalance scheduling.
Do not add portfolio allocation logic.
Do not add new trading behavior.
Do not change sizing because of REBALANCE yet.
```

Reason: you are in the architecture-cleanup phase. The safest move is to make the system’s intent model explicit everywhere before adding another live strategy path.

Your order should be:

```text
1. Purpose plumbing
2. Database + notification visibility
3. Dedupe tests
4. Trade explainability page / notification format
5. Only then consider rebalance logic
```

So the next move is simple: **tell it to thread `order_purpose` through every call site and record schema touchpoint, with REBALANCE as plumbing only.**
