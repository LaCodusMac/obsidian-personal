---
title: "Backup — Plex"
type: resource
tags: [resource, backup-task, backups]
status: not-started
priority: medium
host: "NUC10 (confirmed)"
---

Back up the **config/database**, not the media bulk (media lives on the Synology and is huge; re-scanning is fine). This preserves libraries, watch history, collections, and settings.

## What to back up
The Plex "Application Support" dir (`Plex Media Server/`), especially:
- `Plug-in Support/Databases/` (the SQLite DBs — libraries + watch state)
- `Preferences.xml`
- Skip the `Cache/` and `Media/` (thumbnails/transcodes) dirs — regenerable, bloats the backup.

## Pre-backup hook
Plex uses SQLite; safest is a brief stop or its DB backup. Simple version:
```bash
systemctl stop plexmediaserver   # optional but avoids a torn DB
# ...restic runs...
systemctl start plexmediaserver
```
Or back up during low-use hours and accept the small risk.

## Fill into the pattern ([[Backups]])
- `<name>` = `plex`
- `<PATHS>` = the Plex config dir, excluding `Cache/` and `Media/`

## Restore test
Restore config to a test Plex, confirm libraries + watch history appear (pointing at the same Synology media paths).

## Status
- [ ] Confirm Plex config path on NUC10
- [ ] Script (+ optional stop/start) + timer, excluding Cache/Media
- [ ] Test-restore

## Related

- Area: [[Backups]]
- Context: [[Self-Hosted Software]], [[Network Stack]], [[NUC10]]
