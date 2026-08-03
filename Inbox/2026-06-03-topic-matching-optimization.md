---
date: 2026-06-03
source: chatgpt
title: "Topic Matching Optimization"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Add explicit topic keywords

Create a file like:

nano kalshi-watch/narrative_topics.py

Add:

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

**ChatGPT:** Yes, this is a good change and likely addresses one of Hermes' biggest weaknesses right now: poor topic matching.

From your logs, Hermes is frequently treating unrelated headlines as narrative support:

- Bear attack in Japan influencing geopolitics
- Alabama congressional map story appearing in elections generally
- Generic political stories being attached to Iran or Ukraine markets

Instead of relying purely on embeddings/similarity, adding a hard keyword layer first is a good filter.

Example:

```python
# narrative_topics.py

TOPIC_KEYWORDS = {
    "iran": [
        "iran", "tehran", "khamenei", "nuclear deal",
        "uranium", "strait of hormuz", "hormuz",
        "missile", "drone"
    ],
    "ukraine": [
        "ukraine", "russia", "putin", "zelensky",
        "kyiv", "moscow", "ceasefire"
    ],
    "fed": [
        "fed", "federal reserve", "powell",
        "fomc", "rate cut", "rate hike", "inflation"
    ],
    "jobs": [
        "payrolls", "jobs report", "unemployment",
        "jobless claims", "labor market"
    ],
    "elections": [
        "election", "senate", "house",
        "supreme court", "voting map",
        "congressional map"
    ],
}
```

Then create a matcher:

```python
from narrative_topics import TOPIC_KEYWORDS

def topic_match(text: str, topic: str) -> bool:
    text = text.lower()

    for keyword in TOPIC_KEYWORDS.get(topic, []):
        if keyword.lower() in text:
            return True

    return False
```

And filter narratives before scoring:

```python
headline_text = f"{headline} {summary}"

if not topic_match(headline_text, market_topic):
    continue
```

I would actually go one step further:

### Tier 1 — Hard keyword match

Require at least one keyword hit.

### Tier 2 — Embedding similarity

Only run expensive semantic scoring after the keyword gate passes.

```python
if not topic_match(text, market_topic):
    continue

similarity = embedding_similarity(text, market_description)

if similarity < 0.55:
    continue
```

This dramatically reduces false positives.

For your specific bot, I'd also add:

```python
"iran": [
    ...
    "israel",
    "idf",
    "iranian",
    "iran-israel",
    "iaea"
]
```

```python
"ukraine": [
    ...
    "donbas",
    "crimea",
    "russian forces",
    "ukrainian forces"
]
```

```python
"fed": [
    ...
    "cpi",
    "pce",
    "interest rates",
    "treasury yield"
]
```

The biggest improvement would be making narrative support conditional on:

1. Topic keyword match
2. Similarity threshold
3. Trusted source threshold

That would have prevented many of the bizarre narrative matches shown in your recent Hermes summaries and should improve both trade quality and confidence scoring.
