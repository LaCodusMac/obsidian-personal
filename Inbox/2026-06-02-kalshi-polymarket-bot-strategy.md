---
date: 2026-06-02
source: chatgpt
title: "Kalshi Polymarket Bot Strategy"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** I’d do both, but with different goals:

- Stick with Kalshi as the execution/trading venue for now
- Add Polymarket as a read-only data source / signal source

That gives you more data without blowing up the bot architecture or regulatory/compliance assumptions.

My recommendation

1. Keep Kalshi as the main bot target

Kalshi is already wired up:

- collector
- signal generation
- demo trader
- risk rules
- frequency rules
- position monitor
- exits
- local DB lifecycle

So the fastest path to actual testing is still improving Kalshi throughput, fills, candidate quality, and exit behavior.

Also, Kalshi is the cleaner place to eventually move from demo to real because it is a regulated exchange. Polymarket trading is a different stack: crypto wallet, CLOB auth, USDC, chain/settlement concerns, and likely more legal/geographic complications.

2. Add Polymarket for more market data

Polymarket is very useful as a data feed:

- It has many more markets.
- Prices are public and easy to query.
- Orderbooks and history are available through public APIs.
- No auth needed for read-only collection.
- It can provide cross-market sentiment and alternative probability estimates.

Good uses:

- Compare Kalshi price vs Polymarket price on similar events.
- Use Polymarket volume/price movement as a narrative or momentum signal.
- Use Polymarket to discover market themes Kalshi might also list.
- Build a cross-market dataset for outcome scoring and probability calibration.

3. Don’t try to trade Polymarket yet

Not yet. I’d avoid building execution there until the Kalshi bot is stable.

Reasons:

- Trading requires wallet/auth/signing.
- More operational failure modes.
- Position accounting is different.
- Settlement and liquidity behavior differs.
- It will distract from fixing the core signal/risk/execution loop.

Best next move

I’d add a Polymarket read-only collector that stores:

- event title
- market question
- outcomes
- yes/no prices
- volume
- liquidity
- open interest if available
- CLOB token IDs
- condition ID
- timestamps

Then we can use that data in two ways:

1. Market discovery: find active/high-volume events worth watching.
2. Kalshi signal enrichment: if a related Polymarket market moves sharply, boost or flag the Kalshi candidate.

Practical staged plan

Phase 1: Read-only Polymarket ingestion

Build a simple collector that hits:

- Gamma API for markets/events
- CLOB API for prices/orderbooks
- Data API for trades/open interest if useful

Store in a new SQLite table, maybe:

- polymarket_events
- polymarket_markets
- polymarket_snapshots
- polymarket_orderbooks

Phase 2: Cross-market matching

Try to match Polymarket markets to Kalshi markets by:

- keywords
- event dates
- entities
- market category
- maybe embeddings later

Phase 3: Signal enrichment

Use Polymarket as an input to Kalshi signals:

- “Polymarket probability moved +8% in 30 minutes”
- “Polymarket volume spiked”
- “Polymarket/Kalshi price divergence is large”
- “Polymarket has liquidity confirming the event is active”

Phase 4: Only later, consider Polymarket execution

Once the bot is profitable/stable in demo-style Kalshi testing, then maybe build Polymarket execution.

Bottom line

I would not abandon Kalshi. You’ve already got the system almost working there.

But yes — I’d absolutely start pulling Polymarket read-only data now. It’s probably the best next dataset to improve trade frequency and candidate quality without adding too much execution risk.

**ChatGPT:** I think that's a solid roadmap, and it aligns with where Hermes appears to be today.

Looking at your recent logs, the biggest issue isn't a lack of markets—it's that Hermes is finding candidates but rejecting almost all of them due to regime, narrative confirmation, outcome sample requirements, and execution filters. Adding Polymarket execution wouldn't fix those bottlenecks.

Where Polymarket could help immediately is with **signal confidence and market discovery**.

### What I'd prioritize first

#### 1. Increase Kalshi opportunity throughput
You've already started doing this with:

```python
signals = get_signals(limit=limit, lookback_minutes=lookback_minutes)
```

and increasing the service limit from 1 to 5–10.

That alone may generate more demo trades than adding an entirely new venue.

---

#### 2. Bootstrap regime statistics
This is still one of the biggest blockers I see.

Your logs frequently show:

> blocked: not enough regime-specific outcome samples

Hermes is behaving conservatively because it doesn't have enough historical evidence.

A Polymarket collector could help here indirectly by:

- providing more market examples
- providing additional probability movement data
- allowing replay/backtesting

But I'd still build a dedicated shadow-trading framework for Hermes so it can accumulate thousands of regime observations quickly.

---

#### 3. Use Polymarket for divergence detection
This is probably the highest-value feature.

Example:

Kalshi:

> Iran Deal YES = 57¢

Polymarket equivalent:

> Iran Deal YES = 68¢

Now Hermes can calculate:

```text
cross_market_edge = 11%
```

and flag:

> "Kalshi materially cheaper than comparable market"

That becomes a new signal source rather than a trading venue.

---

#### 4. Use Polymarket for narrative validation
Right now many candidates fail with messages like:

> market move lacks topic-matched high-trust narrative confirmation

Polymarket volume spikes could become an additional confirmation layer:

- Kalshi moving
- Polymarket moving
- News moving

When all three align, confidence increases.

---

### Architecture I'd build

New collectors:

```text
polymarket_collector.py
```

New tables:

```sql
polymarket_events
polymarket_markets
polymarket_snapshots
polymarket_orderbooks
```

Then later:

```sql
market_correlations
cross_market_matches
```

And eventually:

```text
cross_market_signal.py
```

which feeds Hermes.

---

### One caution

I would avoid trying to automatically match markets too aggressively at first.

For example:

- "Will US agree to Iran deal in 2026?"
- "Will US and Iran sign a nuclear agreement before Dec 31?"

These sound similar but may settle differently.

Start with:

- exact topic tags
- manual mappings
- keyword confidence scores

before allowing the signals to influence trading decisions.

---

### If I were allocating development time today

1. Fix exit behavior completely (Hermes monitor reliability)
2. Increase candidate throughput (`limit=5–10`)
3. Add shadow-trade outcome collection
4. Add Polymarket read-only ingestion
5. Add Kalshi ↔ Polymarket divergence signals
6. Add narrative confirmation from Polymarket volume
7. Consider Polymarket execution much later

Given the state of your Hermes logs, steps 1–3 are likely to increase trade quality and frequency faster than building a second execution venue. Polymarket becomes most valuable as a **data source that improves Hermes' decision-making**, not as a replacement for Kalshi.
