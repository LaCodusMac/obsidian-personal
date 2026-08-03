---
date: 2026-05-09
source: chatgpt
title: "Unauthenticated Requests Explained"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Making Unauthenticated Requests
Kalshi provides several public endpoints that don’t require API keys. These endpoints allow you to access market data directly from our production servers at. What does this mean in laymans terms

**ChatGPT:** In simple terms:

Kalshi has some data that anyone on the internet can look at without needing to log in or prove who they are.

“Unauthenticated requests” means:
- You can ask Kalshi’s servers for certain information
- Without an API key, password, or account authentication

Usually this is read-only/public information like:
- Current market prices
- Market listings
- Trading volume
- Event data
- Order book snapshots

Think of it like:
- Looking at a public website page = unauthenticated
- Accessing your bank account = authenticated

For your suspicious trading project, this is important because it means you can start collecting and analyzing market data immediately without building a full secure login system first.

Example conceptually:

You send:
```bash
GET https://api.elections.kalshi.com/trade-api/v2/markets
```

Kalshi sends back:
```json
{
  "markets": [
    {
      "ticker": "TRUMP2028",
      "yes_bid": 42,
      "volume": 120000
    }
  ]
}
```

No login required.

But if you wanted to:
- place trades
- view private account info
- manage orders
- access balances

…then you’d need authenticated requests using API keys and signatures.

For what you're building:
- Phase 1 can probably rely heavily on unauthenticated endpoints
- You can scrape/order-book monitor/watch volume anomalies
- Later phases may use authenticated APIs for automation or paper trading systems

The big advantage:
You can prototype your detection engine fast without worrying about security/auth infrastructure first.

**You:** How should I be addressing my first step then

**ChatGPT:** Your **first step** should be:

**Build a simple Kalshi public market data collector.**

Do **not** start with “AI suspicious detection” yet. Start by reliably pulling and saving market data.

### Step 1 goal

Create a script that can:

1. Pick a small group of markets
2. Pull public data from Kalshi
3. Save snapshots every minute
4. Store them in a simple database or CSV
5. Let you look back and say: “what changed?”

### What to collect first

For each market, save:

```text
timestamp
market_ticker
yes_bid
yes_ask
no_bid
no_ask
last_price
volume
open_interest
liquidity
status
```

If available later, also collect:

```text
order book levels
recent trades
price movement
volume changes
```

### Best beginner version

Start with **one Python script**.

Use:

```text
Python
requests
SQLite
pandas later
```

Do **not** start with:

```text
Kafka
Postgres
React dashboard
machine learning
live alerts
```

That comes later.

### Your first working milestone

You want to be able to run:

```bash
python collect_kalshi.py
```

And have it create something like:

```text
kalshi_data.db
```

With rows like:

```text
2026-05-09 10:01, MARKET-ABC, 42, 44, 56, 58, 43, 12000
2026-05-09 10:02, MARKET-ABC, 45, 47, 53, 55, 46, 12400
2026-05-09 10:03, MARKET-ABC, 61, 64, 36, 39, 62, 18100
```

Then your suspicious logic becomes simple:

```text
Did price move a lot?
Did volume spike?
Did it happen suddenly?
Was the market normally quiet before?
```

### My recommended Phase 1 stack

```text
Python collector
SQLite database
Cron job or loop timer
Basic anomaly score
CSV export
```

That is enough to start.

Your first “suspicious” rule can be:

```text
Flag market if volume jumps 5x above its recent average
AND price moves more than 10 cents within 5 minutes
```

Example:

```text
Normal:
Volume per minute: 20 contracts
Price movement: 1-2 cents

Suspicious:
Volume per minute: 600 contracts
Price movement: 18 cents
```

That is the first real version of your bot.

**You:** Help me build that out

**ChatGPT:** We’ll build this as a very small Phase 1: one Python collector, one SQLite database, and one simple anomaly rule. I’ll verify the current Kalshi public endpoint shape first so the starter code matches the real API.

**ChatGPT:** Start with this exact project structure:

```bash
mkdir kalshi-watch
cd kalshi-watch
python3 -m venv venv
source venv/bin/activate
pip install requests pandas
```

Kalshi’s public market-data base URL is:

```text
https://external-api.kalshi.com/trade-api/v2
```

Their docs say public market data can be requested without auth/API keys, including markets and order book snapshots. citeturn682558search0turn682558search1

Create this file:

```bash
nano collect_kalshi.py
```

Paste this:

```python
import requests
import sqlite3
import time
from datetime import datetime, timezone

BASE_URL = "https://external-api.kalshi.com/trade-api/v2"
DB_NAME = "kalshi_data.db"

# Start with one active series. You can change this later.
SERIES_TICKER = "KXHIGHNY"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS market_snapshots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        ticker TEXT,
        title TEXT,
        status TEXT,
        yes_bid INTEGER,
        yes_ask INTEGER,
        no_bid INTEGER,
        no_ask INTEGER,
        last_price INTEGER,
        volume INTEGER,
        open_interest INTEGER,
        liquidity INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        ticker TEXT,
        reason TEXT,
        score REAL
    )
    """)

    conn.commit()
    conn.close()


def get_markets():
    url = f"{BASE_URL}/markets"
    params = {
        "series_ticker": SERIES_TICKER,
        "status": "open",
        "limit": 100
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json().get("markets", [])


def save_snapshot(market):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    now = datetime.now(timezone.utc).isoformat()

    cur.execute("""
    INSERT INTO market_snapshots (
        timestamp, ticker, title, status,
        yes_bid, yes_ask, no_bid, no_ask,
        last_price, volume, open_interest, liquidity
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        now,
        market.get("ticker"),
        market.get("title"),
        market.get("status"),
        market.get("yes_bid"),
        market.get("yes_ask"),
        market.get("no_bid"),
        market.get("no_ask"),
        market.get("last_price"),
        market.get("volume"),
        market.get("open_interest"),
        market.get("liquidity")
    ))

    conn.commit()
    conn.close()


def check_anomaly(ticker):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    SELECT timestamp, last_price, volume
    FROM market_snapshots
    WHERE ticker = ?
    ORDER BY id DESC
    LIMIT 6
    """, (ticker,))

    rows = cur.fetchall()
    conn.close()

    if len(rows) < 6:
        return

    newest = rows[0]
    oldest = rows[-1]

    newest_price = newest[1]
    oldest_price = oldest[1]
    newest_volume = newest[2]
    oldest_volume = oldest[2]

    if newest_price is None or oldest_price is None:
        return

    price_change = abs(newest_price - oldest_price)
    volume_change = (newest_volume or 0) - (oldest_volume or 0)

    score = price_change + (volume_change / 100)

    if price_change >= 10 and volume_change >= 100:
        save_alert(
            ticker,
            f"Price moved {price_change} cents and volume increased by {volume_change} contracts recently.",
            score
        )


def save_alert(ticker, reason, score):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    now = datetime.now(timezone.utc).isoformat()

    cur.execute("""
    INSERT INTO alerts (timestamp, ticker, reason, score)
    VALUES (?, ?, ?, ?)
    """, (now, ticker, reason, score))

    conn.commit()
    conn.close()

    print(f"ALERT: {ticker} | {reason} | score={score}")


def main():
    init_db()

    while True:
        print("Collecting market snapshots...")

        try:
            markets = get_markets()

            for market in markets:
                save_snapshot(market)
                check_anomaly(market.get("ticker"))

            print(f"Saved {len(markets)} market snapshots.")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(60)


if __name__ == "__main__":
    main()
```

Run it:

```bash
python collect_kalshi.py
```

What this does:

```text
Every 60 seconds:
1. Pulls open Kalshi markets from one series
2. Saves price/volume data into SQLite
3. Compares the latest snapshot to the last few minutes
4. Creates an alert if price and volume jump together
```

To inspect your data:

```bash
sqlite3 kalshi_data.db
```

Then:

```sql
SELECT * FROM market_snapshots ORDER BY id DESC LIMIT 10;
```

Check alerts:

```sql
SELECT * FROM alerts ORDER BY id DESC;
```

Your real first milestone is not “detect manipulation” yet.

Your first milestone is:

```text
Can I collect clean market data for 24 hours without the script breaking?
```

Once that works, the next upgrade is adding order book snapshots, because Kalshi’s order book endpoint shows YES and NO bid levels for a specific market. citeturn682558search1

**You:** Please add comments to let me know what the code is doing

**ChatGPT:** ```python
# Import libraries we need
import requests              # Used to make HTTP requests to Kalshi's API
import sqlite3               # Built-in lightweight database
import time                  # Lets us pause between API calls
from datetime import datetime, timezone


# Base URL for Kalshi public API
BASE_URL = "https://external-api.kalshi.com/trade-api/v2"

# SQLite database file name
DB_NAME = "kalshi_data.db"

# Market series to monitor
# You can change this later to other Kalshi series
SERIES_TICKER = "KXHIGHNY"


# -----------------------------
# DATABASE SETUP
# -----------------------------
def init_db():

    # Connect to SQLite database
    conn = sqlite3.connect(DB_NAME)

    # Cursor lets us execute SQL commands
    cur = conn.cursor()

    # Create table to store market snapshots
    # IF NOT EXISTS prevents recreating the table every run
    cur.execute("""
    CREATE TABLE IF NOT EXISTS market_snapshots (

        # Auto-incrementing unique ID
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        # Timestamp of snapshot
        timestamp TEXT,

        # Market identifier
        ticker TEXT,

        # Human-readable market title
        title TEXT,

        # Market status (open, closed, settled, etc.)
        status TEXT,

        # Best YES buy price
        yes_bid INTEGER,

        # Best YES sell price
        yes_ask INTEGER,

        # Best NO buy price
        no_bid INTEGER,

        # Best NO sell price
        no_ask INTEGER,

        # Most recent trade price
        last_price INTEGER,

        # Total contracts traded
        volume INTEGER,

        # Current open positions
        open_interest INTEGER,

        # Available liquidity in market
        liquidity INTEGER
    )
    """)

    # Table for suspicious activity alerts
    cur.execute("""
    CREATE TABLE IF NOT EXISTS alerts (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        # Time alert occurred
        timestamp TEXT,

        # Market ticker that triggered alert
        ticker TEXT,

        # Human-readable explanation
        reason TEXT,

        # Numeric anomaly score
        score REAL
    )
    """)

    # Save database changes
    conn.commit()

    # Close database connection
    conn.close()


# -----------------------------
# GET MARKET DATA FROM KALSHI
# -----------------------------
def get_markets():

    # Endpoint URL
    url = f"{BASE_URL}/markets"

    # Query parameters sent to Kalshi
    params = {

        # Which market category to search
        "series_ticker": SERIES_TICKER,

        # Only open markets
        "status": "open",

        # Maximum number of markets returned
        "limit": 100
    }

    # Send GET request to API
    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    # Throw error if request failed
    response.raise_for_status()

    # Return market list from JSON response
    return response.json().get("markets", [])


# -----------------------------
# SAVE MARKET SNAPSHOT
# -----------------------------
def save_snapshot(market):

    # Connect to database
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Current UTC timestamp
    now = datetime.now(timezone.utc).isoformat()

    # Insert market snapshot into database
    cur.execute("""
    INSERT INTO market_snapshots (

        timestamp,
        ticker,
        title,
        status,
        yes_bid,
        yes_ask,
        no_bid,
        no_ask,
        last_price,
        volume,
        open_interest,
        liquidity

    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        now,

        market.get("ticker"),
        market.get("title"),
        market.get("status"),

        market.get("yes_bid"),
        market.get("yes_ask"),

        market.get("no_bid"),
        market.get("no_ask"),

        market.get("last_price"),

        market.get("volume"),

        market.get("open_interest"),

        market.get("liquidity")
    ))

    # Save changes
    conn.commit()

    # Close database
    conn.close()


# -----------------------------
# DETECT SUSPICIOUS ACTIVITY
# -----------------------------
def check_anomaly(ticker):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Get latest 6 snapshots for this market
    # Ordered newest first
    cur.execute("""
    SELECT timestamp, last_price, volume
    FROM market_snapshots
    WHERE ticker = ?
    ORDER BY id DESC
    LIMIT 6
    """, (ticker,))

    rows = cur.fetchall()

    conn.close()

    # Need at least 6 snapshots
    if len(rows) < 6:
        return

    # Most recent snapshot
    newest = rows[0]

    # Snapshot from ~5 minutes ago
    oldest = rows[-1]

    newest_price = newest[1]
    oldest_price = oldest[1]

    newest_volume = newest[2]
    oldest_volume = oldest[2]

    # Skip if prices missing
    if newest_price is None or oldest_price is None:
        return

    # Calculate price movement
    price_change = abs(newest_price - oldest_price)

    # Calculate recent volume increase
    volume_change = (
        (newest_volume or 0)
        - (oldest_volume or 0)
    )

    # Very basic anomaly score
    # You will improve this later
    score = price_change + (volume_change / 100)

    # Trigger alert if movement large enough
    if price_change >= 10 and volume_change >= 100:

        save_alert(
            ticker,

            f"Price moved {price_change} cents "
            f"and volume increased by "
            f"{volume_change} contracts recently.",

            score
        )


# -----------------------------
# SAVE ALERT
# -----------------------------
def save_alert(ticker, reason, score):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    now = datetime.now(timezone.utc).isoformat()

    # Store alert in database
    cur.execute("""
    INSERT INTO alerts (
        timestamp,
        ticker,
        reason,
        score
    )
    VALUES (?, ?, ?, ?)
    """, (
        now,
        ticker,
        reason,
        score
    ))

    conn.commit()
    conn.close()

    # Print alert to terminal
    print(
        f"ALERT: {ticker} | "
        f"{reason} | "
        f"score={score}"
    )


# -----------------------------
# MAIN LOOP
# -----------------------------
def main():

    # Ensure database exists
    init_db()

    # Infinite loop
    while True:

        print("Collecting market snapshots...")

        try:

            # Pull market data from Kalshi
            markets = get_markets()

            # Process each market
            for market in markets:

                # Save market snapshot
                save_snapshot(market)

                # Check for suspicious behavior
                check_anomaly(
                    market.get("ticker")
                )

            print(
                f"Saved {len(markets)} "
                f"market snapshots."
            )

        except Exception as e:

            # Print any errors
            print(f"Error: {e}")

        # Wait 60 seconds before next pull
        time.sleep(60)


# -----------------------------
# PROGRAM ENTRY POINT
# -----------------------------
# Only run main loop if script directly executed
if __name__ == "__main__":
    main()
```

**You:** where should I run this

**ChatGPT:** Given your setup and experience, the best place to run this is on your Ubuntu server machine — ideally the Lenovo P3 or one of your Intel NUCs running Ubuntu/Docker. You already have experience with Ubuntu, Plex, Docker, and self-hosted services, so this fits naturally into your homelab stack.

## Recommended setup

### Best Option
Run it directly on your Ubuntu server first.

This is easiest for learning/debugging.

Example machines:
- Your Lenovo P3
- Your Ubuntu NUC10i5FNH
- Any always-on Linux box

Later:
- Dockerize it
- Add dashboards
- Add alerting
- Add multiple collectors

But not yet.

---

# Step-by-step setup

## 1. Open terminal on Ubuntu

SSH into the server or use local terminal.

Example:

```bash
ssh ubuntu@192.168.x.x
```

---

## 2. Create project folder

```bash
mkdir kalshi-watch
cd kalshi-watch
```

---

## 3. Create Python virtual environment

This keeps packages isolated.

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Your terminal should now show:

```bash
(venv)
```

---

## 4. Install dependencies

```bash
pip install requests pandas
```

---

## 5. Create the script

```bash
nano collect_kalshi.py
```

Paste the code.

Save with:

```text
CTRL + O
ENTER
CTRL + X
```

---

## 6. Run it

```bash
python collect_kalshi.py
```

You should start seeing:

```text
Collecting market snapshots...
Saved X market snapshots.
```

---

# Check database is working

You should now see:

```bash
ls
```

Including:

```text
kalshi_data.db
```

---

# View stored data

Install sqlite tools if needed:

```bash
sudo apt install sqlite3
```

Open DB:

```bash
sqlite3 kalshi_data.db
```

Run:

```sql
SELECT ticker, last_price, volume
FROM market_snapshots
ORDER BY id DESC
LIMIT 10;
```

Exit:

```sql
.quit
```

---

# Your actual learning goal right now

Not:
```text
"build AI"
```

Instead:
```text
"understand market behavior through stored data"
```

This phase teaches:
- APIs
- Data collection
- Databases
- Time-series thinking
- Signal detection
- Quant-style workflows

Those are the foundations of the suspicious-trading system you actually want.

Later phases become:
1. Better anomaly scoring
2. Order book analysis
3. Live websockets
4. Pattern clustering
5. Event correlation
6. Statistical baselines
7. ML models
8. Automated alerts
9. Trade simulation
10. Strategy engine

But Phase 1 is:
```text
Can I reliably collect and store clean market data?
```

**You:** Can this run on the same machine as my AI models or should I seperate it

**ChatGPT:** Yes — this can run on the **same machine as your AI models** for now.

The Kalshi collector is very lightweight:

```text
CPU: tiny
RAM: tiny
Disk: small at first
Network: tiny
GPU: none
```

So it will not meaningfully affect Ollama/Open WebUI/OpenClaw unless you later make it much heavier.

Best setup for you:

```text
Lenovo P3 / AI machine:
- Ollama / Open WebUI / OpenClaw
- Kalshi collector
- SQLite database for now
```

Separate it later when you add:

```text
Postgres
live websocket collectors
dashboard
multiple markets
alerting
backtesting
large data storage
ML training
```

My recommendation:

```text
Run collector on the AI machine now.
Move it later only if it causes clutter or you want reliability.
```

For the first version, it is better to keep everything simple and running than to over-engineer it.
