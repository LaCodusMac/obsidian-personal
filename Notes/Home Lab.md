---
title: "Home Lab"
aliases: [The Lab]
type: area
tags: [area, homelab, infrastructure]
---

The ongoing home lab — the physical and software infrastructure everything else runs on. This is an **Area** (never "done"), and it's the hub for the hardware, software, and network notes.

## What lives here
- **[[Hardware Inventory]]** — physical equipment: UniFi stack, NUCs, Synology NAS, 3D printer, spare/repurpose machines.
- **[[Self-Hosted Software]]** — the services running: Pi-hole, Plex, and the rest.
- **[[Network Stack]]** — the network topology and service placement (from documentation; not fully current).

## What runs on it
- [[Hermes Agent]] and its modules ([[KalshiWatch]], [[Workout Tracker]], [[Family Bots]]).
- Media, DNS filtering, backups, monitoring.

## Recommended end state (per [[Network Stack]] doc)
Synology for storage/backups · NUC10 for primary Docker apps · NUC8 or OptiPlex for DNS/monitoring/lab · UniFi for VPN and network control · backup laptop as a second copy target.

## ⚠️ Backup status: NONE
Right now **nothing is being backed up** — not [[Hermes Agent]]'s memory/config, not the [[KalshiWatch]] SQLite DB, not this vault. The Synology *can* be a backup target (per [[Network Stack]]) but no job is running. Highest-priority fix for the whole lab. See the **[[Backups]]** area for the full plan + reusable restic/systemd pattern and a per-service note for each thing worth protecting.

## Open Questions / To Do
- **Set up backups** (see above) — do this first.
- 3D printer: [[Prusa Mini]] runs off the gaming PC — fine as-is; note it's outside lab backup coverage.

## Related
- Projects: [[Hermes Agent]], [[KalshiWatch]]
- Areas: [[Backups]]
- Resources: [[Hardware Inventory]], [[Self-Hosted Software]], [[Network Stack]]
