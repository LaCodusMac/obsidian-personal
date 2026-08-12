---
title: "KalshiWatch"
aliases: [Kalshi, Kalshi bot]
type: project
status: active
priority: high
started: 2026-01-01
tags: [project, kalshi, trading, hermes, python]
---

The Kalshi prediction-market watcher and (demo) trading system that runs as a module of [[Hermes Agent]]. It collects market data, generates signals, runs automated demo trades, monitors open positions with exit logic, ingests a narrative feed, and reports out — all controllable and observable through Telegram.

> 📌 I already keep fuller Kalshi documentation inside this vault. This note is the **code-level architecture map** derived from the `KalshiWatch-main` source. Treat my existing Kalshi docs as the source of truth for strategy/history; treat this as the component index. Merge or cross-link when convenient.

## Architecture (from source)
Python (deps: `requests`, `cryptography`, `python-dotenv`), SQLite-backed, with Grafana dashboards for visualization. ~76 Python files. Broken into packages:

- **`services/`** — thin entry points mirroring the systemd units (collector, signal, trader, monitor, reporting). Coordinates other packages; no business logic.
- **`position_monitor/`** — the engine behind `hermes_position_monitor.py`: DB, market normalization, PnL/excursion metrics, position lifecycle, exit-order pricing/lifecycle, and the monitor loop that sends Telegram sell/watch alerts.
- **`trading/`** — the workflow behind `hermes_bridge.py`: `observe` / `recommend` / `demo_execute`, order sizing, execution/error handling, trade records, notifications.
- **`analytics/`** — read-only outcome analysis: `expectancy`, `attribution`, `lane_analysis` (core vs explore vs manual), `regime_analysis`, `snapshots`. Reads signal outcomes / trade recommendations / lifecycle metrics; never places orders.
- **`venues/`** — exchange adapters (`kalshi.py`, `polymarket.py`).

## Telegram control surface
`hermes_telegram_bot.py` — authorizes specific Telegram user IDs, commands include:
- Read: `/status`, `/positions`, `/top`
- Auto-trading control: `/pause_auto`, `/resume_auto`, `/kill_switch`
- Manual orders: `/buy_yes`, `/buy_no`, `/sell`, `/sell_yes`, `/sell_no`

## systemd units (scheduled/always-on)
- `hermes-telegram-bot.service` — the control bot
- `kalshi-watch.service` — market collector
- `hermes-demo-trader.service` + `.timer` — automated demo trading
- `hermes-position-monitor.service` + `.timer` — position monitoring/exits
- `hermes-narrative-ingestor.service` + `.timer` — narrative feed ingest
- `hermes-narrative-report.service` + `.timer` + `hermes-opportunity-report.service` + `.timer` — reporting
- `kalshi-grafana.service` — dashboards

## Safety / config
Config lives in `config.demo.env` (git-ignored; a `.example` ships). Key guardrails in config: `KILL_SWITCH`, `AUTO_TRADING_ENABLED`, `LIVE_TRADING_ENABLED` / `ALLOW_REAL_TRADING` (default off), `RECOMMEND_ONLY`, position/size caps (`MAX_ORDER_SIZE`, `MAX_OPEN_POSITIONS`), frequency caps (`MAX_TRADES_PER_HOUR`/`_PER_DAY`), and an exploration lane with its own bankroll cap. Repo ships a `keys/DO_NOT_USE_LIVE_KEYS.txt` marker — currently a **demo-mode** system.

## Open Questions
- Is it still demo-only, or has live trading been enabled since this snapshot?
- Cross-link my existing in-vault Kalshi docs here.

## Host & backup
Runs on the **Lenovo P3 Mini** alongside [[Hermes Agent]] (confirmed). ⚠️ The SQLite DB is **not currently backed up** — if the P3 Mini dies, all trade history / signal outcomes / lifecycle metrics are lost. **Plan: [[Backup — KalshiWatch]]** (shares the P3 Mini restic repo; see [[Backups]]).

## Related
- Parent: [[Hermes Agent]]
- Areas: [[Home Lab]]
- Resources: [[Self-Hosted Software]], [[Network Stack]]

## Log
- 2026-07-28: Note created from `KalshiWatch-main` source snapshot. Architecture, Telegram commands, systemd units, and config guardrails captured. Cross-link to existing in-vault Kalshi docs pending.
