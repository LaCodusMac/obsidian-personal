---
title: "Backup — KalshiWatch"
type: resource
tags: [resource, backup-task, backups]
status: not-started
priority: high
host: "Lenovo P3 Mini"
related_projects: ["[[KalshiWatch]]"]
related_areas: ["[[Backups]]"]
---

# Backup — KalshiWatch

Protects the [[KalshiWatch]] history: trades, signal outcomes, position-lifecycle metrics, and config. Same host as [[Hermes Agent]], so this can share the P3 Mini restic repo.

## What to back up
- The **SQLite DB** (trade_recommendations, signal_outcomes, position_lifecycle_metrics, etc.).
- `config.demo.env` (⚠️ contains Telegram tokens + Kalshi key refs — treat as secret; the restic repo is encrypted, good).
- `keys/` dir (private key path referenced by `KALSHI_PRIVATE_KEY_PATH`).
- Grafana dashboards are **already in the git repo** as JSON — version-controlled, so lower urgency, but include if the DB source lives outside git.

## Pre-backup hook (important — live SQLite)
```bash
sqlite3 /path/kalshi.db ".backup '/tmp/kalshi.db.bak'"
```
Back up the `.bak`, not the live file, to avoid a torn copy mid-write.

## Fill into the pattern ([[Backups]])
- `<name>` = `kalshiwatch`
- `<PATHS>` = `/tmp/kalshi.db.bak` + config.demo.env + keys/

## Restore test
Restore the DB, open it read-only, confirm recent trades/rows are present.

## Status
- [ ] Confirm DB path
- [ ] Script (with sqlite .backup hook) + timer
- [ ] First test-restore
