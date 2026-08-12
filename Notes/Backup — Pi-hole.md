---
title: "Backup — Pi-hole"
type: resource
tags: [resource, backup-task, backups]
status: not-started
priority: medium
host: "Pi-hole-1 (Raspberry Pi 5, confirmed) — bare-metal package"
---

Small and fast to protect; saves you rebuilding adlists, custom DNS, and settings by hand. Runs on one of the three [[Raspberry Pi 5]] boards — confirmed Pi-hole, not AdGuard Home, and confirmed a **bare-metal package install** rather than a container (2026-08-11), so the paths below are real filesystem paths on the Pi.

> Higher priority than "medium" suggests: this is the **only** DNS resolver on the LAN, so losing it takes name resolution down for everything until it's rebuilt by hand.

## ⚠️ Check the version before trusting the commands below

The admin URL (`https://192.168.1.18/admin/login`) suggests **Pi-hole v6**, ~70% confidence — see [[Pi-hole]] for the reasoning. The commands and paths in this runbook were written for **v5**. If it is v6, both are wrong:

- `pihole -a -t` was replaced by `pihole-FTL --teleporter`
- config consolidated into `/etc/pihole/pihole.toml`; `setupVars.conf` is gone
- `/etc/dnsmasq.d/` is no longer Pi-hole's source of truth

Run `pihole -v` and correct this file before building the job. A backup script that runs cleanly while archiving the wrong directory is the worst outcome available here — it reports success and restores nothing.

## Pre-backup hook (Pi-hole "Teleporter" export)
```bash
# v5:
pihole -a -t /tmp/pihole-teleporter.tar.gz
# v6:
pihole-FTL --teleporter /tmp/pihole-teleporter.tar.gz
```
Then back up `/tmp/pihole-teleporter.tar.gz` plus `/etc/pihole/` (and `/etc/dnsmasq.d/` if v5).

> AdGuard Home instead? Not applicable — confirmed Pi-hole.

## Fill into the pattern ([[Backups]])
- `<name>` = `pihole`
- `<PATHS>` = teleporter archive + `/etc/pihole/` + `/etc/dnsmasq.d/`

## Restore test
Import the teleporter file into a fresh Pi-hole, confirm adlists + custom entries return.

## Status
- [x] Confirm install method on the Pi — **bare-metal package**, confirmed 2026-08-11
- [ ] Run `pihole -v` and correct the paths/commands above for the actual major version
- [ ] Script (with teleporter export) + timer
- [ ] Test-restore

## Related

- Area: [[Backups]]
- Context: [[Raspberry Pi 5]], [[Self-Hosted Software]], [[Network Stack]]
