---
date: 2026-06-08
source: chatgpt
title: "Modify Narrative Topics"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** ls   kalshi-watch
__pycache__                         hermes-telegram-bot.service  scorecards.py
add_narrative_event.py              hermes_bridge.py             signals.py
backfill_severity_normalization.py  hermes_control.py            telegram_notifier.py
backfill_signal_outcomes.py         hermes_order_router.py       test_collect_api_guards.py
collect_kalshi.py                   hermes_position_monitor.py   test_demo_trader_retries.py
config.demo.env                     hermes_reporter.py           test_frequency_rules.py
config.demo.env.example             hermes_telegram_bot.py       test_hermes_order_router.py
demo_trader.py                      kalshi-grafana.service       test_hermes_reporter.py
frequency_rules.py                  kalshi-watch.service         test_hermes_telegram_bot.py
grafana                             kalshi.db                    test_kalshi_demo.py
grafana-13.0.1                      kalshi_data.db               test_market_regimes.py
grafana-13.0.1.linux-amd64.tar.gz   kalshi_data.db-shm           test_narrative_events.py
hermes-demo-trader.service          kalshi_data.db-wal           test_narrative_feed_ingestor.py
hermes-demo-trader.timer            kalshi_watch.lock            test_orderbook_history.py
hermes-narrative-ingestor.service   keys                         test_outcome_risk.py
hermes-narrative-ingestor.timer     list_narrative_sources.py    test_position_monitor.py
hermes-narrative-report.service     mark_position_closed.py      test_severity_scoring.py
hermes-narrative-report.timer       narrative_events.py          test_signals.py
hermes-opportunity-report.service   narrative_feed_ingestor.py   test_telegram_notifier.py
hermes-opportunity-report.timer     narrative_topics.py          venv
hermes-position-monitor.service     requirements.txt
hermes-position-monitor.timer       risk_rules.py

**ChatGPT:** Good — `narrative_topics.py` already exists.

Now check contents:

```bash
cd kalshi-watch
cat narrative_topics.py
```

If it’s empty or wrong, edit it:

```bash
nano narrative_topics.py
```

Paste/update:

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

Save in nano:

```text
Ctrl+O
Enter
Ctrl+X
```

Then test syntax:

```bash
python3 -m py_compile narrative_topics.py
```

Next likely file to modify is:

```bash
nano narrative_feed_ingestor.py
```

That’s probably where we need to import `TOPIC_KEYWORDS` and improve topic matching.

**You:** cd kalshi-watch
cat narrative_topics.py
TOPIC_KEYWORDS = {
    "iran": {
        "iran",
        "iranian",
        "iran-israel",
        "tehran",
        "khamenei",
        "nuclear deal",
        "uranium",
        "strait of hormuz",
        "hormuz",
        "missile",
        "drone",
        "israel",
        "idf",
        "iaea",
        "sanction",
        "sanctions",
    },
    "ukraine": {
        "ukraine",
        "ukrainian forces",
        "russia",
        "russian forces",
        "putin",
        "zelensky",
        "kyiv",
        "moscow",
        "ceasefire",
        "donbas",
        "crimea",
        "nato",
    },
    "fed": {
        "fed",
        "federal reserve",
        "powell",
        "fomc",
        "rate cut",
        "rate hike",
        "inflation",
        "cpi",
        "pce",
        "interest rates",
        "treasury yield",
    },
    "jobs": {
        "payrolls",
        "payroll",
        "jobs report",
        "unemployment",
        "jobless claims",
        "labor market",
        "employment situation",
    },
    "elections": {
        "election",
        "campaign",
        "candidate",
        "ballot",
        "poll",
        "senate",
        "house",
        "supreme court",
        "voting map",
        "congressional map",
    },
    "election": {
        "election",
        "campaign",
        "candidate",
        "ballot",
        "poll",
        "senate",
        "house",
        "supreme court",
        "voting map",
        "congressional map",
    },
    "israel": {
        "israel",
        "idf",
        "gaza",
        "hamas",
        "ceasefire",
        "truce",
    },
    "taiwan": {
        "taiwan",
        "china",
        "beijing",
        "taipei",
    },
    "cpi": {
        "cpi",
        "consumer price",
        "inflation",
    },
    "crypto": {
        "bitcoin",
        "btc",
        "ethereum",
        "eth",
        "crypto",
        "doge",
        "xrp",
        "solana",
    },
}

MARKET_KEYWORDS = frozenset(
    keyword
    for keywords in TOPIC_KEYWORDS.values()
    for keyword in keywords
)


def topic_match(text: str, topic: str | None) -> bool:
    if not topic:
        return False

    lowered = (text or "").lower()
    for keyword in TOPIC_KEYWORDS.get(topic, ()):
        if keyword.lower() in lowered:
            return True

    return False


def matched_topic(text: str, default_topic: str | None = None) -> str | None:
    lowered = (text or "").lower()
    best_topic = default_topic
    best_hits = 0

    for topic, keywords in TOPIC_KEYWORDS.items():
        hits = sum(1 for keyword in keywords if keyword in lowered)
        if hits > best_hits:
            best_topic = topic
            best_hits = hits

    return best_topic


def text_has_market_keyword(text: str) -> bool:
    lowered = (text or "").lower()
    return any(keyword in lowered for keyword in MARKET_KEYWORDS)

**ChatGPT:** That file is actually pretty solid. It's much more complete than the simple version we discussed.

A few observations:

### Good
- Iran/Hormuz coverage is much better.
- Fed includes CPI/PCE.
- Ukraine includes NATO, Crimea, Donbas.
- Crypto has the major assets.
- `matched_topic()` scores by keyword count instead of first match.

### Potential Problems

#### 1. Duplicate election topic

You have both:

```python
"elections": {...}
```

and

```python
"election": {...}
```

Those are effectively the same topic.

That can create weird behavior where:

```python
matched_topic("Supreme Court voting map")
```

might return `"election"` on one event and `"elections"` on another.

I'd keep only one:

```python
"elections": {...}
```

and remove:

```python
"election": {...}
```

---

#### 2. Israel and Iran overlap

Iran contains:

```python
"israel",
"idf",
```

and Israel contains:

```python
"israel",
"idf",
```

This means almost every Israel headline will score as Iran too.

Example:

```
IDF launches operation in Gaza
```

Scores:

- israel = 2 hits
- iran = 2 hits

You may get incorrect topic assignment.

I'd remove:

```python
"israel",
"idf",
```

from the Iran topic.

Keep:

```python
"iran-israel"
```

because that specifically identifies the conflict.

---

#### 3. China/Taiwan

Current:

```python
"taiwan": {
    "taiwan",
    "china",
    "beijing",
    "taipei",
}
```

The word:

```python
"china"
```

is extremely broad.

Any China headline becomes Taiwan.

Example:

```
China manufacturing data misses expectations
```

would incorrectly become a Taiwan event.

I'd split:

```python
"china": {...}
"taiwan": {...}
```

or remove `"china"` from Taiwan.

---

### What I'd check next

Find where topic matching is actually used:

```bash
grep -R "matched_topic(" .
```

and

```bash
grep -R "topic_match(" .
```

and post the output.

My suspicion is that the real Hermes issue is not this file anymore—it's that `narrative_feed_ingestor.py` or `narrative_events.py` is not using these topic scores aggressively enough when attaching news to Kalshi markets. The keyword dictionary itself looks mostly fine.

**You:** I want to know what you think of the file structure trying to analyze the project

**ChatGPT:** File structure looks **good for a serious prototype**, but it’s starting to outgrow “flat script folder” mode.

My read:

**Good signs**
- Clear core modules: `collect_kalshi.py`, `signals.py`, `risk_rules.py`, `frequency_rules.py`, `demo_trader.py`, `hermes_bridge.py`, `hermes_position_monitor.py`
- Tests exist for most important areas.
- Systemd service/timer files are checked into the project, which is useful.
- Narrative system is becoming its own subsystem: `narrative_events.py`, `narrative_topics.py`, `narrative_feed_ingestor.py`
- Telegram/manual control is separated: `hermes_telegram_bot.py`, `hermes_order_router.py`, `hermes_control.py`

**Main problem**
Everything is in one big root directory. It is still understandable, but it will get messy fast.

I’d eventually reorganize like this:

```text
kalshi-watch/
  hermes/
    __init__.py
    collector.py
    signals.py
    risk_rules.py
    frequency_rules.py
    trader.py
    bridge.py
    position_monitor.py
    order_router.py
    telegram_bot.py

    narrative/
      __init__.py
      events.py
      topics.py
      feed_ingestor.py
      sources.py

    reporting/
      __init__.py
      reporter.py
      telegram_notifier.py

    db/
      __init__.py
      migrations/
      models.py

  tests/
    test_risk_rules.py
    test_signals.py
    test_position_monitor.py
    ...

  systemd/
    hermes-demo-trader.service
    hermes-demo-trader.timer
    hermes-position-monitor.service
    ...

  config/
    config.demo.env.example

  scripts/
    backfill_signal_outcomes.py
    backfill_severity_normalization.py
    mark_position_closed.py
    add_narrative_event.py

  data/
    kalshi_data.db
```

But I **would not reorganize immediately** unless the bot is stable. Moving files can break imports/services.

Priority order I’d use:

1. **Leave structure mostly as-is for now**
2. Fix behavior: exits, bad notifications, bad topic matching, risk spam
3. Add a `README.md` explaining what each file does
4. Move service files into `systemd/`
5. Move tests into `tests/`
6. Only later convert the app into a real `hermes/` package

The current structure says: “working solo bot prototype with decent testing.”  
The next structure should say: “maintainable trading system.”

**You:** [Unit]
Description=Hermes Kalshi demo trader
After=network-online.target kalshi-watch.service
Wants=network-online.target

[Service]
Type=oneshot
WorkingDirectory=/home/carlthellama/kalshi-watch
ExecStart=/home/carlthellama/kalshi-watch/venv/bin/python /home/carlthellama/kalshi-watch/hermes_bridge.py demo_execute --limit 10 --lookback-minutes 15
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
(END)

**ChatGPT:** That service file looks valid.

It runs the demo trader **once per trigger**:

```bash
hermes_bridge.py demo_execute --limit 10 --lookback-minutes 15
```

So the timer is what makes it repeat.

Check the timer:

```bash
cat /etc/systemd/system/hermes-demo-trader.timer
```

You want something like:

```ini
[Unit]
Description=Run Hermes demo trader every minute

[Timer]
OnBootSec=30
OnUnitActiveSec=60
Unit=hermes-demo-trader.service

[Install]
WantedBy=timers.target
```

Then reload and restart:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now hermes-demo-trader.timer
sudo systemctl restart hermes-demo-trader.timer
```

Check it:

```bash
systemctl status hermes-demo-trader.timer
journalctl -u hermes-demo-trader.service -n 100 --no-pager
```

Also, you’re viewing it in `less`. Press:

```text
q
```

to exit.
