---
date: 2026-05-12
source: chatgpt
title: "SQL tour for Kalshi bot"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** help me work with sql while we still do not have a dash board. give me a tour

**ChatGPT:** Absolutely — while you don’t have Grafana/dashboard views yet, SQLite can basically be your “manual dashboard.” I’ll give you a practical tour: how to open it, inspect tables, view recent rows, summarize markets, and spot weird movement.

**ChatGPT:** Here’s your **SQLite tour** for the Kalshi bot.

## 1. Open the database

From your Kalshi bot folder:

```bash
sqlite3 kalshi_bot.db
```

If your DB has a different name, list files:

```bash
ls
ls *.db
```

Inside SQLite, turn on readable mode:

```sql
.headers on
.mode column
.timer on
```

## 2. See what tables exist

```sql
.tables
```

Then inspect a table:

```sql
.schema market_snapshots
```

Useful command:

```sql
.schema
```

That shows all table structures.

## 3. View newest market data

```sql
SELECT *
FROM market_snapshots
ORDER BY id DESC
LIMIT 10;
```

Cleaner version:

```sql
SELECT 
  ticker,
  title,
  yes_bid,
  yes_ask,
  last_price,
  volume,
  timestamp
FROM market_snapshots
ORDER BY id DESC
LIMIT 20;
```

## 4. Look at one market over time

Replace the ticker:

```sql
SELECT 
  timestamp,
  yes_bid,
  yes_ask,
  last_price,
  volume
FROM market_snapshots
WHERE ticker = 'KXHIGHNY-26MAY11-B62.5'
ORDER BY timestamp DESC
LIMIT 50;
```

## 5. Find highest-volume markets

```sql
SELECT 
  ticker,
  title,
  MAX(volume) AS latest_volume
FROM market_snapshots
GROUP BY ticker
ORDER BY latest_volume DESC
LIMIT 20;
```

## 6. Find markets with big price changes

This compares the lowest and highest observed price per ticker:

```sql
SELECT
  ticker,
  title,
  MIN(last_price) AS low_price,
  MAX(last_price) AS high_price,
  MAX(last_price) - MIN(last_price) AS price_range
FROM market_snapshots
WHERE last_price IS NOT NULL
GROUP BY ticker
ORDER BY price_range DESC
LIMIT 20;
```

## 7. Find wide spreads

Wide spread = yes_ask minus yes_bid.

```sql
SELECT
  ticker,
  title,
  yes_bid,
  yes_ask,
  yes_ask - yes_bid AS spread,
  timestamp
FROM market_snapshots
WHERE yes_bid IS NOT NULL
  AND yes_ask IS NOT NULL
ORDER BY spread DESC
LIMIT 20;
```

## 8. Find recent “interesting” rows

High volume, low price, possibly weird:

```sql
SELECT
  ticker,
  title,
  yes_bid,
  yes_ask,
  last_price,
  volume,
  timestamp
FROM market_snapshots
WHERE volume > 50000
ORDER BY timestamp DESC
LIMIT 30;
```

## 9. Count how much data you have

```sql
SELECT COUNT(*) FROM market_snapshots;
```

Rows per ticker:

```sql
SELECT 
  ticker,
  COUNT(*) AS snapshots
FROM market_snapshots
GROUP BY ticker
ORDER BY snapshots DESC;
```

## 10. Export to CSV

From inside SQLite:

```sql
.headers on
.mode csv
.output market_snapshots_export.csv

SELECT *
FROM market_snapshots;

.output stdout
```

Then exit:

```sql
.quit
```

## Best “manual dashboard” command

Use this often:

```sql
SELECT 
  ticker,
  yes_bid,
  yes_ask,
  last_price,
  volume,
  timestamp
FROM market_snapshots
ORDER BY id DESC
LIMIT 25;
```

Think of each row as a **snapshot in time**. Your dashboard later will mostly be prettier versions of these same SQL queries.

**You:** Runtime error: database is locked (5)

**ChatGPT:** That usually means:

- your watcher/bot is actively writing to SQLite
- and your current SQLite session is trying to read/write at the same time.

SQLite only allows limited concurrent access.

Because your Kalshi watcher is likely continuously inserting snapshots, this is normal.

## Quick Fixes

### Option 1 — Open SQLite in read-only mode (best for viewing)

Exit SQLite:

```sql
.quit
```

Then reopen:

```bash
sqlite3 -readonly kalshi_bot.db
```

Now your queries should work much more reliably while the bot runs.

---

## Option 2 — Enable WAL mode (VERY recommended)

This is the real fix for bots + dashboards.

Open normally:

```bash
sqlite3 kalshi_bot.db
```

Run:

```sql
PRAGMA journal_mode=WAL;
```

You should see:

```text
wal
```

Then exit:

```sql
.quit
```

WAL mode allows:
- simultaneous readers
- while the bot writes

This is how SQLite is usually run for monitoring systems.

---

## Option 3 — Set a timeout

Inside SQLite:

```sql
.timeout 5000
```

This tells SQLite:
> “wait up to 5 seconds if locked.”

---

# Recommended Setup For You

Since your bot continuously collects market data:

1. Enable WAL mode once
2. Use read-only sessions for viewing
3. Later connect Grafana to the same DB

That stack works very well for lightweight monitoring.

---

## Check if WAL mode is enabled

```sql
PRAGMA journal_mode;
```

If it says:

```text
wal
```

you’re good.

---

## See if your watcher is actively writing

From Linux terminal:

```bash
watch -n 2 'sqlite3 -readonly kalshi_bot.db "SELECT COUNT(*) FROM market_snapshots;"'
```

That refreshes every 2 seconds so you can literally watch rows increase live.

Very useful for sanity-checking ingestion.

**You:** Error: unable to open database "kalshi_bot.db": unable to open database file

**ChatGPT:** That means you’re probably not in the folder where the database actually lives.

## Step 1 — Find the database

From terminal:

```bash
find ~ -name "*.db"
```

or more targeted:

```bash
find ~ -name "kalshi_bot.db"
```

You’ll likely get something like:

```text
/home/jake/kalshi/data/kalshi_bot.db
```

---

## Step 2 — Change into that folder

Example:

```bash
cd /home/jake/kalshi/data
```

Then verify:

```bash
ls
```

You should see:

```text
kalshi_bot.db
```

---

## Step 3 — Open read-only

```bash
sqlite3 -readonly kalshi_bot.db
```

---

# Faster Method

Once you find it, you can open directly:

```bash
sqlite3 -readonly /full/path/to/kalshi_bot.db
```

Example:

```bash
sqlite3 -readonly /home/jake/kalshi/data/kalshi_bot.db
```

---

# Useful Linux Habit

Check where you are:

```bash
pwd
```

List files:

```bash
ls -lah
```

You’ll use these constantly while building the bot stack.

---

# Once You’re Back In

Immediately run:

```sql
.headers on
.mode column
.timeout 5000
```

Then:

```sql
SELECT COUNT(*) FROM market_snapshots;
```

If that works, your database is healthy.

**You:** __pycache__  collect_kalshi.py  kalshi-watch.service  kalshi_data.db  kalshi_data.db-journal  kalshi_watch.lock  venv

**ChatGPT:** Your database is named:

```bash
kalshi_data.db
```

Open it like this:

```bash
sqlite3 -readonly kalshi_data.db
```

Then run:

```sql
.headers on
.mode column
.timeout 5000
.tables
```

Your lock/journal files mean the bot is probably running:

```text
kalshi_data.db-journal
kalshi_watch.lock
```

So avoid opening `kalshi_data.db` normally unless you need to change settings. For viewing data, use:

```bash
sqlite3 -readonly kalshi_data.db
```

Then try:

```sql
SELECT COUNT(*) FROM market_snapshots;
```

**You:** 64242

**ChatGPT:** Perfect — that means your database currently has:

```text
64,242 rows
```

So your ingestion pipeline is working.

Now let’s start using SQL like an actual monitoring console.

# Your Most Useful Queries

---

# 1. Watch newest market updates live

```sql
SELECT
  ticker,
  yes_bid,
  yes_ask,
  last_price,
  volume,
  timestamp
FROM market_snapshots
ORDER BY id DESC
LIMIT 20;
```

This becomes your:
- live tape
- feed monitor
- sanity checker

---

# 2. See most active markets

```sql
SELECT
  ticker,
  MAX(volume) AS volume
FROM market_snapshots
GROUP BY ticker
ORDER BY volume DESC
LIMIT 20;
```

This tells you:
- where money is flowing
- what markets are attracting attention

---

# 3. Find volatile markets

```sql
SELECT
  ticker,
  MIN(last_price) AS low,
  MAX(last_price) AS high,
  MAX(last_price) - MIN(last_price) AS move
FROM market_snapshots
GROUP BY ticker
ORDER BY move DESC
LIMIT 20;
```

This is VERY important later.

You’re basically asking:

> “Which markets moved the most?”

That’s the beginning of anomaly detection.

---

# 4. Find stale or dead markets

```sql
SELECT
  ticker,
  COUNT(*) AS snapshots
FROM market_snapshots
GROUP BY ticker
ORDER BY snapshots ASC
LIMIT 20;
```

Useful for:
- bad feeds
- inactive markets
- collection issues

---

# 5. Watch one market evolve

Replace ticker:

```sql
SELECT
  timestamp,
  yes_bid,
  yes_ask,
  last_price,
  volume
FROM market_snapshots
WHERE ticker = 'KXHIGHNY-26MAY11-B62.5'
ORDER BY timestamp DESC
LIMIT 100;
```

This becomes:
- your manual candlestick chart
- your trade history
- your replay system

---

# 6. Find suspicious spreads

```sql
SELECT
  ticker,
  yes_bid,
  yes_ask,
  yes_ask - yes_bid AS spread,
  volume
FROM market_snapshots
WHERE yes_bid IS NOT NULL
AND yes_ask IS NOT NULL
ORDER BY spread DESC
LIMIT 20;
```

Wide spreads can mean:
- low liquidity
- manipulation
- stale pricing
- scared market makers

---

# 7. See how fast data is coming in

```sql
SELECT
  MIN(timestamp),
  MAX(timestamp)
FROM market_snapshots;
```

Then:

```sql
SELECT COUNT(*) / 60.0 AS rows_per_second
FROM market_snapshots;
```

(if roughly 1 minute of data exists)

---

# 8. Learn the structure of your table

VERY important habit:

```sql
PRAGMA table_info(market_snapshots);
```

This shows:
- every column
- type
- indexes

You’ll use this constantly while building models.

---

# Most Important SQL Concepts For Your Project

## SELECT

Choose columns.

```sql
SELECT ticker, volume
```

---

## WHERE

Filter rows.

```sql
WHERE volume > 10000
```

---

## ORDER BY

Sort.

```sql
ORDER BY volume DESC
```

---

## LIMIT

Only show top N rows.

```sql
LIMIT 20
```

---

## GROUP BY

Aggregate markets together.

```sql
GROUP BY ticker
```

Critical for analytics.

---

## Aggregate functions

```sql
MAX()
MIN()
AVG()
COUNT()
SUM()
```

These are the backbone of dashboards.

---

# What You’re Actually Building

Right now:
- SQLite = storage engine
- SQL = analysis layer
- terminal = dashboard

Later:
- Grafana = visualization layer
- Python analytics = intelligence layer
- ML/anomaly system = detection layer

You’re already building the foundation of a real market surveillance stack.

**You:** ORDER BY move DESC
LIMIT 20;
KXSOLD-26MAY1217-T92.9999|0|96|96
KXVOTEFEDCHAIR-27-CCOO|0|89|89
KXCHINAANNOUNCE-26MAY-MAY17-FENT|0|79|79
KXCHINAANNOUNCE-26MAY-MAY17-BOT|0|79|79
KXCHINAANNOUNCE-26MAY-MAY17-SOYA|0|70|70
KXHYPE15M-26MAY112330-30|2|56|54
KXBNB15M-26MAY112330-30|35|85|50
KXETH15M-26MAY112330-30|3|52|49
KXSOL15M-26MAY112330-30|0|47|47
KXBTC15M-26MAY112330-30|1|44|43
KXBTC-26MAY1200-B80150|0|42|42
KXXRP15M-26MAY112330-30|1|40|39
KXHIGHNY-26MAY11-T62|65|99|34
KXDOGE15M-26MAY112330-30|1|33|32
KXHIGHNY-26MAY11-B62.5|1|28|27
KXBNB15M-26MAY112345-45|9|35|26
KXTRUEV-26MAY12-T1244.69|62|87|25
KXJETFUEL-26MAY13-T4.15|30|54|24
KXAAAGASD-26MAY12-4.495|75|99|24
KXLEAVETISCH-27JAN01|54|76|22

**ChatGPT:** This is where things start getting interesting.

You just generated your first real **market volatility ranking**.

The query:

```sql
MAX(last_price) - MIN(last_price) AS move
```

is showing:
> “How much did this market swing during the time period stored in the DB?”

That is a foundational surveillance metric.

# How To Read These Results

Example:

```text
KXSOLD-26MAY1217-T92.9999 | 0 | 96 | 96
```

Means:

| Metric | Value |
|---|---|
| Lowest observed price | 0 |
| Highest observed price | 96 |
| Total movement | 96 |

That market basically:
- started “impossible”
- then became “almost certain”
- OR vice versa

Huge move.

---

# What This Suggests

Some of these are:
- event-resolution markets
- crypto microstructure markets
- prediction spike markets
- news reaction markets

Those are exactly where unusual trading patterns appear.

---

# Important Insight

Right now your query is mixing:

- old resolved markets
- active markets
- dead markets
- extremely short-term markets

So the next step is filtering.

---

# Better Query: Active High-Movement Markets

Try:

```sql
SELECT
  ticker,
  MIN(last_price) AS low,
  MAX(last_price) AS high,
  MAX(last_price) - MIN(last_price) AS move,
  MAX(volume) AS volume
FROM market_snapshots
WHERE volume > 1000
GROUP BY ticker
HAVING move > 15
ORDER BY move DESC
LIMIT 25;
```

This removes some garbage/noise.

---

# Why This Matters For Your Suspicious Activity Idea

You said earlier you care about:

- unusually large trades
- weird movement
- sudden confidence shifts
- suspicious positioning before events

This query is literally step 1.

You are identifying:
- abnormal market behavior
- markets with asymmetric information
- fast repricing events

---

# Next-Level Queries You’ll Want Soon

## 1. Sudden volume spikes

```sql
SELECT
  ticker,
  MAX(volume) - MIN(volume) AS volume_change
FROM market_snapshots
GROUP BY ticker
ORDER BY volume_change DESC
LIMIT 20;
```

This shows:
> “Where did money suddenly appear?”

Very useful.

---

# 2. Most rapidly updating markets

```sql
SELECT
  ticker,
  COUNT(*) AS updates
FROM market_snapshots
GROUP BY ticker
ORDER BY updates DESC
LIMIT 20;
```

This shows:
- highly active feeds
- rapidly repricing markets

---

# 3. Markets near certainty

```sql
SELECT
  ticker,
  last_price,
  volume
FROM market_snapshots
WHERE last_price > 95
ORDER BY volume DESC
LIMIT 20;
```

Interesting because:
- insider information often pushes markets toward certainty early

---

# 4. Markets collapsing

```sql
SELECT
  ticker,
  MIN(last_price) AS low,
  MAX(last_price) AS high
FROM market_snapshots
GROUP BY ticker
HAVING high > 80
AND low < 20
ORDER BY high - low DESC
LIMIT 20;
```

These are:
- narrative reversals
- failed expectations
- major news shocks

---

# What You’re Beginning To Build

You are slowly creating:

| Layer | Purpose |
|---|---|
| SQLite | Raw historical tape |
| SQL | Market analytics |
| Python | Pattern detection |
| Grafana | Visualization |
| ML | Suspiciousness scoring |

That is genuinely how professional monitoring stacks evolve.
