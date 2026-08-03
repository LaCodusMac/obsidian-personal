---
date: 2026-05-27
source: chatgpt
title: "Bug Fix: Scoring Logic"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** The key bug is in signals.py: it already records regime_label in signal_outcomes, but candidate scoring joins
  outcomes only by market_group,event_type. I’m changing that so regime-specific outcomes are primary, and broad
  historical outcomes are only a fallback that risk can reject in abnormal regimes.

**ChatGPT:** Exactly — that’s the right fix.

Your current bug is basically:

**“This signal type worked historically”**
instead of:
**“This signal type worked historically in this market regime.”**

Change scoring priority to:

1. `market_group + event_type + regime_label`
2. fallback to `market_group + event_type`
3. reject/penalize fallback if current regime is abnormal, thin, volatile, stale, or unknown

In plain terms, Hermes should say:

> “I only trust past outcomes if the current market environment matches the environment where those outcomes happened.”

For abnormal regimes, fallback history should not be enough to pass risk. It can inform the score, but it should require extra confirmation like liquidity, spread, recent win rate, or manual/alert-only mode.

Good rule:

```text
if regime_specific_samples >= min_samples:
    use regime-specific outcome stats
elif regime_label in abnormal_regimes:
    block or alert-only
else:
    use broad fallback stats with penalty
```

This should help stop the bot from over-trusting old “high severity” patterns that only worked under normal liquidity/volatility.
