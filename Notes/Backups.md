---
title: "Backups"
type: area
tags: [area, backups, infrastructure, restic]
related_areas: ["[[Home Lab]]"]
related_resources: ["[[Backup — Hermes]]", "[[Backup — KalshiWatch]]", "[[Backup — Obsidian Vault]]", "[[Backup — Plex]]", "[[Backup — Pi-hole]]", "[[Backup — UniFi]]", "[[Backup — Synology Config]]"]
---

# Backups

The ongoing backup responsibility for the whole [[Home Lab]]. **Current reality: nothing is running yet.** This hub holds the reusable pattern; each service below has its own short note with the specifics (what to grab, pre-backup hook, restore test).

## Strategy: 3-2-1
- **3** copies of anything that matters.
- **2** different media/locations.
- **1** off-site.

Concretely: source data lives on its host (P3 Mini / NUC / Synology), **copy 1** is a restic repo on the **Synology**, **copy 2 off-site** is a restic `copy` to cloud (Backblaze B2 via rclone) or a rotated external drive kept elsewhere.

## Status
```dataview
TABLE status, priority, host
FROM "04-Resources"
WHERE contains(tags, "backup-task")
SORT priority DESC
```

## Reusable pattern (restic + systemd timer)
This mirrors how [[KalshiWatch]] already runs (`.service` + `.timer`). Do this once per host; each service note just fills in **paths** and an optional **pre-backup hook**.

### 1. One-time repo init (on the host being backed up)
```bash
# Store the repo password once, root-only
printf 'CHANGE-ME-long-random' | sudo install -m 600 /dev/stdin /root/.restic-pass

# Point restic at a folder on the Synology over SFTP
export RESTIC_REPOSITORY="sftp:backup@synology:/volume1/backups/restic/$(hostname)"
export RESTIC_PASSWORD_FILE=/root/.restic-pass
restic init
```
> Set up an SSH key from the host to a dedicated `backup` user on the Synology first (`ssh-copy-id backup@synology`) so it's non-interactive. Enable SSH + a shared folder `backups` in DSM.

### 2. Per-service backup script — `/usr/local/bin/backup-<name>.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail
export RESTIC_REPOSITORY="sftp:backup@synology:/volume1/backups/restic/$(hostname)"
export RESTIC_PASSWORD_FILE=/root/.restic-pass

# --- optional pre-backup hook (per service; e.g. sqlite .backup, pihole export) ---
# <PRE_HOOK>

restic backup <PATHS> \
  --tag <name> \
  --exclude-caches \
  --exclude '*.tmp'

# retention
restic forget --tag <name> \
  --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune

# OFF-SITE copy (set up a second repo once, e.g. B2), then uncomment:
# restic -r b2:my-bucket:$(hostname) --password-file /root/.restic-pass copy --tag <name>
```
Make it executable: `sudo chmod +x /usr/local/bin/backup-<name>.sh`

### 3. systemd unit + timer
`/etc/systemd/system/backup-<name>.service`
```ini
[Unit]
Description=restic backup — <name>
Wants=network-online.target
After=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup-<name>.sh
Nice=10
IOSchedulingClass=idle
```
`/etc/systemd/system/backup-<name>.timer`
```ini
[Unit]
Description=Daily restic backup — <name>

[Timer]
OnCalendar=*-*-* 03:30:00
RandomizedDelaySec=1800
Persistent=true

[Install]
WantedBy=timers.target
```
Enable:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now backup-<name>.timer
systemctl list-timers 'backup-*'
```

### 4. Prove it works (do this, don't skip)
```bash
restic snapshots --tag <name>
restic restore latest --tag <name> --target /tmp/restore-test-<name>
# verify the files are actually there and openable
```
> A backup you've never restored is a hope, not a backup. Test-restore each service once after setup, then re-test quarterly.

## Setup order (highest value first)
1. [[Backup — Hermes]] — the memory is irreplaceable.
2. [[Backup — KalshiWatch]] — trade history / signal outcomes.
3. [[Backup — Obsidian Vault]] — this brain.
4. [[Backup — Pi-hole]], [[Backup — UniFi]] — small, fast, saves painful reconfig.
5. [[Backup — Plex]] — config/watch history (not the media bulk).
6. [[Backup — Synology Config]] + wire up the off-site leg for real 3-2-1.

## Related
- Area: [[Home Lab]]
