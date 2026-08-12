---
title: "Backup — UniFi"
type: resource
tags: [resource, backup-task, backups]
status: not-started
priority: medium
host: "UniFi Cloud Key (confirmed)"
---

Protects network config: VLANs, firewall rules, Wi-Fi/SSIDs, VPN setup — painful to reconstruct from memory. The controller runs on the [[UniFi Cloud Key]] appliance. (See [[Network Stack]].)

## Approach
UniFi has its own backup:
- In the UniFi Network app: **Settings → System → Backups** → enable **Auto Backup** (keep several, download `.unf`).
- Then pull those `.unf` files into restic so they land on the Synology + off-site, not just on the controller.

## Fill into the pattern ([[Backups]])
- `<name>` = `unifi`
- `<PATHS>` = the auto-backup export dir / downloaded `.unf` files
- Controller is an appliance, not a container you manage — so the `.unf` export *is* the backup. There's no host volume to snapshot, which makes the auto-backup step non-optional.

## Restore test
Spin up / factory-adopt into a test controller and restore a `.unf`, or at minimum confirm the `.unf` opens and is recent. Also **store admin credentials + VLAN map** somewhere safe (the network doc worksheet).

## Status
- [ ] Enable auto-backup in UniFi
- [ ] Pull .unf into restic
- [ ] Verify a backup file is current

## Related

- Area: [[Backups]]
- Context: [[UniFi Cloud Key]], [[Hardware Inventory]], [[Network Stack]]
