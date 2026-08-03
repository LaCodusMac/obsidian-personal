---
title: "Backup — UniFi"
type: resource
tags: [resource, backup-task, backups]
status: not-started
priority: medium
host: "UniFi Gateway / controller"
related_resources: ["[[Network Stack]]", "[[Hardware Inventory]]"]
related_areas: ["[[Backups]]"]
---

# Backup — UniFi

Protects network config: VLANs, firewall rules, Wi-Fi/SSIDs, VPN setup — painful to reconstruct from memory. (See [[Network Stack]].)

## Approach
UniFi has its own backup:
- In the UniFi Network app: **Settings → System → Backups** → enable **Auto Backup** (keep several, download `.unf`).
- Then pull those `.unf` files into restic so they land on the Synology + off-site, not just on the controller.

## Fill into the pattern ([[Backups]])
- `<name>` = `unifi`
- `<PATHS>` = the auto-backup export dir / downloaded `.unf` files
- If controller runs as a container/host you manage, also back up its config/data volume.

## Restore test
Spin up / factory-adopt into a test controller and restore a `.unf`, or at minimum confirm the `.unf` opens and is recent. Also **store admin credentials + VLAN map** somewhere safe (the network doc worksheet).

## Status
- [ ] Enable auto-backup in UniFi
- [ ] Pull .unf into restic
- [ ] Verify a backup file is current
