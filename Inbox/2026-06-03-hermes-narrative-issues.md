---
date: 2026-06-03
source: chatgpt
title: "Hermes Narrative Issues"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Hermes Narrative Check

Window: last 6h
News events: 12 shown
Hot markets checked: 10
Recent filled demo trades: 8

Source mix
- geopolitics: events=51 trusted=5 official=0 avgscore=22.1
- elections: events=11 trusted=1 official=0 avgscore=21.9
- fed: events=1 trusted=1 official=0 avgscore=48.8

*Most relevant headlines*
- elections/general rank=2 score=48.8 unclear medium | CNBC: Supreme Court allows Alabama to use congressional map that dilutes Black vote
- geopolitics/general rank=2 score=48.8 bullish\yes medium | BBC: Watch: Man attacked by bear at steel works in Japan
- geopolitics/ukraine rank=2 score=48.8 bullish_yes medium | BBC: Putin remains uncompromising on Ukraine, but is public discourse on war changing in Russia?
- geopolitics/general rank=2 score=48.8 unclear medium | CNBC: Cassidy: Pulte not 'competent' for intelligence director role
- geopolitics/iran rank=2 score=48.8 bullish_yes medium | BBC: US military says it fired missile at Iran-bound oil tanker
- geopolitics/general rank=2 score=48.8 unclear medium | CNBC: DOJ 'not moving forward' with Trump anti-weaponization fund, Blanche says
- fed/fed rank=2 score=48.8 unclear medium | BBC: Trump taps housing official Bill Pulte to be US spymaster
- geopolitics/iran rank=4 score=19.2 bullish_yes low | Google News Geo Search: U.S. military says it has ‘defeated’ Iran missile and drone attacks in Gulf - The Japan Times

Trade-linked context
- KXPAYROLLS-26MAY-T90000 SELL_DEMO_YES yes 1@54c lane=core | manual review exit: direct YES sell at latest yes_bid after EXIT_STUCK; exchange_response={"order": 
- KXPAYROLLS-26MAY-T90000 BUY_DEMO_YES yes 1@55c lane=explore | low liquidity move + Price movement is large relative to available liquidity (111.00).; passed explo
- KXLEAVESTARMER-26SEP01 BUY_DEMO_YES yes 1@54c lane=explore | low liquidity move + Price movement is large relative to available liquidity (48.00).; passed explor
- KXVENEZUELALEADER-26DEC31-NMAD BUY_DEMO_YES yes 1@68c lane=explore | low liquidity move + Price movement is large relative to available liquidity (252.00).; passed explo
- KXECONSTATU3-26MAY-T4.4 BUY_DEMO_YES yes 1@29c lane=explore | volume spike + Volume increased by 1100 contracts.; passed exploration tiny-probe checks (relaxed='h

Market narrative checks
- No candidate-specific narrative checks triggered.

**ChatGPT:** This output actually highlights one of Hermes' biggest current weaknesses:

### The narrative engine is collecting headlines, but not connecting them to tradable markets.

The giveaway is the last line:

> **"No candidate-specific narrative checks triggered."**

Despite:
- 51 geopolitics events
- 12 news events in 6 hours
- Iran headlines
- Ukraine headlines
- Fed headlines
- 8 recent demo trades

Hermes still didn't find any narrative-to-market linkage.

---

## What looks wrong

### 1. Garbage relevance matching

Examples:

> BBC: Watch: Man attacked by bear at steel works in Japan

classified as:

> geopolitics/general bullish_yes

That headline has essentially zero prediction-market value.

Likewise:

> Trump taps housing official Bill Pulte to be US spymaster

classified as:

> fed/fed

which isn't a Fed story.

This suggests the classifier is mostly keyword-driven and not actually understanding the article.

Result:

Hermes gets lots of events.

But most are noise.

---

### 2. Trusted source count is extremely low

You collected:

- 51 geopolitics events

but only:

- 5 trusted

That's under 10%.

For a narrative strategy that's a problem.

The bot is basically saying:

> "I saw a lot of headlines but almost none were high confidence."

---

### 3. The trades aren't being justified by narratives

Look at the trade reasons:

> low liquidity move

> price movement is large relative to available liquidity

> volume spike

Those are market-structure signals.

Not narrative signals.

So currently Hermes is trading:

- volume
- liquidity
- price changes

while news ingestion is mostly sitting on the sidelines.

---

## The Iran example

This headline:

> U.S. military says it has defeated Iran missile and drone attacks in Gulf

should potentially affect:

- Iran nuclear deal markets
- Strait of Hormuz markets
- Gulf conflict escalation markets

Yet Hermes says:

> No candidate-specific narrative checks triggered.

That means either:

### A) Topic mapping failed

or

### B) No market was linked to "Iran"

or

### C) Narrative score never exceeded threshold

---

## Why the bot keeps opening odd trades

Take:

> KXVENEZUELALEADER-26DEC31-NMAD @ 68¢

Reason:

> Price movement is large relative to available liquidity

That's not a thesis.

That's:

> "Something moved."

The bot still appears to be trading anomalies rather than information.

---

## What I'd inspect next

Look at the narrative matching table/database.

Questions:

1. Does Hermes have a topic map?

Example:

```python
{
    "iran": [
        "KXUSAIRANAGREEMENT",
        "KXHORMUZ",
        "KXIRAN"
    ]
}
```

2. When an Iran article arrives:

```python
headline -> topic -> market
```

is that mapping occurring?

3. How many candidate markets received:

```python
narrative_score > 0
```

during this run?

If the answer is near zero, then narrative ingestion is effectively disconnected from trading.

---

## What I think the report really says

The good news:

- News collection is working.
- Scoring is working.
- Event storage is working.
- Trade logging is working.

The bad news:

- Narrative relevance is weak.
- Classification quality is weak.
- Market linkage is weak.
- Trades are still mostly driven by liquidity/volume anomalies.

So Hermes today looks more like a **microstructure trading bot with a news feed attached**, rather than a true **event-driven prediction market trader**.

That last line:

> **No candidate-specific narrative checks triggered**

is probably the most important line in the entire report because it suggests the narrative engine is not yet influencing trade decisions in a meaningful way.

**You:** How to fix step by ste[

**ChatGPT:** We can fix this by separating the problem into three layers: headline quality, topic/market linking, and trade gating. I’ll give you a step-by-step path that improves signal quality without weakening your risk rules.

**ChatGPT:** Do it in this order.

## Step 1 — Stop garbage headlines from scoring

Add a headline filter before scoring.

Block headlines containing stuff like:

```python
"Watch:"
"video"
"live updates"
"opinion"
"analysis"
"who is"
"what we know"
```

Also block weak topics unless they match a market keyword.

Example rule:

```python
if "bear" in headline.lower() and "market" not in headline.lower():
    reject_event("non_market_noise")
```

This prevents “man attacked by bear” from becoming geopolitics.

---

## Step 2 — Add explicit topic keywords

Create a file like:

```bash
nano kalshi-watch/narrative_topics.py
```

Add:

```python
TOPIC_KEYWORDS = {
    "iran": [
        "iran", "tehran", "khamenei", "nuclear deal",
        "uranium", "strait of hormuz", "hormuz", "missile", "drone"
    ],
    "ukraine": [
        "ukraine", "russia", "putin", "zelensky", "kyiv",
        "moscow", "ceasefire"
    ],
    "fed": [
        "fed", "federal reserve", "powell", "fomc",
        "rate cut", "rate hike", "inflation"
    ],
    "jobs": [
        "payrolls", "jobs report", "unemployment",
        "jobless claims", "labor market"
    ],
    "elections": [
        "election", "senate", "house", "supreme court",
        "voting map", "congressional map"
    ],
}
```

---

## Step 3 — Add market-to-topic mapping

Create:

```python
MARKET_TOPICS = {
    "KXUSAIRANAGREEMENT": ["iran"],
    "KXHORMUZ": ["iran"],
    "KXPAYROLLS": ["jobs", "fed"],
    "KXECONSTATU3": ["jobs", "fed"],
    "KXLEAVESTARMER": ["elections"],
    "KXVENEZUELALEADER": ["geopolitics"],
}
```

This is the missing bridge.

Right now Hermes sees news and markets separately.

This connects them.

---

## Step 4 — Require candidate-specific matches

Before Hermes allows a narrative boost, require:

```python
event_topic in market_topics
```

Example:

```python
def narrative_matches_market(event_topic, ticker):
    for prefix, topics in MARKET_TOPICS.items():
        if ticker.startswith(prefix):
            return event_topic in topics
    return False
```

Then:

```python
if not narrative_matches_market(event_topic, ticker):
    narrative_score = 0
```

This stops random geopolitics headlines from boosting unrelated trades.

---

## Step 5 — Add a “no narrative, no core trade” rule

For core trades:

```python
if lane == "core" and narrative_score <= 0:
    block("core trade requires candidate-specific narrative")
```

For explore trades, allow tiny probes only:

```python
if lane == "explore":
    size = 1
    max_hold_minutes = min(max_hold_minutes, 5)
```

So Hermes can still test, but not treat noise as conviction.

---

## Step 6 — Print debug output

Add this to the narrative check report:

```text
Candidate narrative links:
ticker | matched_topic | headline | source | score | accepted/rejected reason
```

Example:

```text
KXHORMUZ | iran | US military fires missile at Iran-bound tanker | BBC | 48.8 | accepted
KXPAYROLLS | iran | US military fires missile... | BBC | 48.8 | rejected_topic_mismatch
```

This will make the issue obvious every time.

---

## Step 7 — Re-run Hermes Narrative Check

After the fix, you want to see:

```text
Market narrative checks
- KXHORMUZ matched iran headline
- KXUSAIRANAGREEMENT matched iran headline
- KXPAYROLLS no candidate narrative
```

Not:

```text
No candidate-specific narrative checks triggered.
```

---

## The main fix

You need this logic:

```python
headline -> topic -> matching market ticker -> narrative score
```

Right now Hermes is closer to:

```python
headline -> broad category -> generic score
```

That is why it is confused.
