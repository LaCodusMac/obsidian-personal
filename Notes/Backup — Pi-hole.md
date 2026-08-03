---
title: "Backup — Pi-hole"
type: resource
tags: [resource, backup-task, backups]
status: not-started
priority: medium
host: "NUC8 or wherever Pi-hole runs"
related_resources: ["[[Self-Hosted Software]]"]
related_areas: ["[[Backups]]"]
---

# Backup — Pi-hole

Small and fast to protect; saves you rebuilding adlists, custom DNS, and settings by hand. (Confirm it's Pi-hole vs AdGuard Home — see [[Self-Hosted Software]].)

## Pre-backup hook (Pi-hole "Teleporter" export)
```bash
# CLI teleporter export → a dated archive
pihole -a -t /tmp/pihole-teleporter.tar.gz
```
Then back up `/tmp/pihole-teleporter.tar.gz` plus `/etc/pihole/` and `/etc/dnsmasq.d/`.

> AdGuard Home instead? Just back up its `AdGuardHome.yaml` and `data/` dir.

## Fill into the pattern ([[Backups]])
- `<name>` = `pihole`
- `<PATHS>` = teleporter archive + `/etc/pihole/` + `/etc/dnsmasq.d/`

## Restore test
Import the teleporter file into a fresh Pi-hole, confirm adlists + custom entries return.

## Status
- [ ] Script (with teleporter export) + timer
- [ ] Test-restore
