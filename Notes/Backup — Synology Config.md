---
title: "Backup — Synology Config"
type: resource
tags: [resource, backup-task, backups]
status: not-started
priority: medium
host: "Synology NAS"
---

The Synology is the **backup target** for everything else — which means it needs its own config backup **and** an off-site copy, or a single NAS failure/theft/fire takes out both the originals' copy and the NAS config.

## Two parts
1. **DSM config export** — Control Panel → Update & Restore → **Configuration Backup** → export the `.dss` (users, shares, task settings). Small; keep copies off the NAS.
2. **Off-site leg for the restic repos** — this is the "1" in 3-2-1. Options:
   - **Hyper Backup** (DSM) → Backblaze B2 / another cloud, or → a second Synology/USB drive rotated off-site.
   - Or `restic copy` from each host into a cloud repo (see [[Backups]] pattern, off-site line).

> Until this off-site leg exists, you technically have 2-1-0 — everything's copy sits on one box in one place.

## Status
- [ ] Export DSM `.dss` config, store off-NAS
- [ ] Choose off-site method (Hyper Backup → B2, or restic copy)
- [ ] Enable + verify first off-site run

## Related

- Area: [[Backups]]
- Context: [[Hardware Inventory]], [[Network Stack]]
