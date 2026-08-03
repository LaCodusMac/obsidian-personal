---
date: 2026-05-24
source: chatgpt
title: "Arbitrage Bet Explanation"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** What’s an arbritrage bet

**ChatGPT:** An arbitrage bet (usually called an “arb”) is when you place bets on **all possible outcomes** of an event at different sportsbooks or markets in a way that guarantees a profit no matter what happens.

The idea is:
- One sportsbook has odds that are slightly “wrong”
- Another sportsbook has different odds
- You exploit the gap between them

Example:

Fight:
- Fighter A: +120 on one sportsbook
- Fighter B: +120 on another sportsbook

Those odds together create a mathematical overlap where both sides pay more than they should.

If you bet the right amounts on each side:
- Fighter A wins → profit
- Fighter B wins → profit

You’re basically acting like a mini-market maker instead of a gambler.

Here’s a simplified example:

| Bet | Odds | Stake |
|---|---|---|
| Team A | +110 | $100 |
| Team B | +110 | $100 |

Total risk = $200

If either side wins:
- Payout = $210
- Guaranteed profit = $10

True arbitrage opportunities are usually:
- Small profit margins (1–5%)
- Short-lived
- Found by software/scanners
- More common in live betting or prediction markets like entity["company","Kalshi","prediction market platform"] and sportsbooks disagreeing with each other

There are a few important catches:
- Books may limit or ban “arb” bettors
- Odds can change before both bets are placed
- Liquidity can be low
- Fees/slippage can kill the profit
- Some “arbs” are fake because of rules differences (OT included vs not included, void rules, etc.)

Since you’ve been working with market anomaly detection and Kalshi-style data, arbitrage is closely related to:
- spread monitoring
- pricing inefficiencies
- latency between markets
- suspicious order flow
- liquidity imbalances

That’s actually one of the reasons people build bots around prediction markets.
