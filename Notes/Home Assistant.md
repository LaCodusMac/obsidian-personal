---
title: "Home Assistant"
aliases: [HA, HASS, HomeAssistant, homeassistant, home automation]
type: service
status: active
host: "HAOS VM on [[Proxmox]] (NUC8i7BEH) — 192.168.1.169"
tags: [homelab, automation, smart-home]
---

The home automation platform, running as a **HAOS virtual machine under [[Proxmox]]** on the NUC8i7BEH, at `192.168.1.169`. Confirmed 2026-08-11.

## Current state

- IP: `192.168.1.169` · Hostname: `homeassistant` · Network: Default VLAN
- **Install method: HAOS** (Home Assistant Operating System) as a full VM — the appliance install, not supervised and not a container. This matters: HAOS manages its own OS and updates, and it has a first-class built-in backup system
- Hypervisor: [[Proxmox]] on the Intel NUC8i7BEH at `192.168.1.10`
- MAC: `02:ff:9d:be:23:38` — locally-administered prefix, i.e. a virtual NIC. This is what independently confirmed "VM" before Mac said so
- Switch path: **USW 24 PoE, port 20**, GbE — shared with the Proxmox host, since the VM is bridged. It has no port of its own
- 24h internet activity: 921 KB — low, consistent with a local-only automation workload
- ⚠️ Unrecorded: which integrations are configured, which physical devices it controls, VM disk size, whether HA is pinned to a version
- ⚠️ **Not backed up.** Nothing in [[Backups]] covers this VM

## Depends on

- [[Proxmox]] — the hypervisor it runs on
- [[Network Stack]] — bridged onto the Default network via USW 24 PoE port 20

## Gotchas

- **No backup coverage.** A Home Assistant config is months of accumulated automations, entity renames, and dashboard layout that exist nowhere else and cannot be reconstructed from memory. Because this is **HAOS**, both layers are easy and worth having independently:
  - **HA's own backup** — Settings → System → Backups. Schedulable, writes a tarball, and restores onto *any* HAOS instance regardless of hypervisor. This is the portable one.
  - **Proxmox `vzdump`** — snapshots the whole VM to [[Synology NAS]]. Restores the machine, not just the config.

  Neither exists yet. The HA-native one takes about two minutes to enable and is the higher-value of the two, because it survives replacing the hypervisor entirely.
- Being a VM means its uptime is bounded by the [[Proxmox]] host's — the NUC8i7BEH, which is un-monitored and un-backed-up. The thing controlling the house depends on a box nobody is watching.
- **`.169` is inside the DHCP pool (`.100`–`.200`), unlike the rest of the infrastructure.** Every other lab machine sits below `.100` where the DHCP server can't hand its address to anything else. This one doesn't, so a lost reservation means HA moves *and* another device can claim `.169`. Renumbering below `.100` — `.11`, alongside its [[Proxmox]] host at `.10` — brings it in line. Do it before the Hermes → Home Assistant integration exists and starts depending on the address.
- HAOS auto-updates its own OS and supervisor. Generally good, but it means the VM can change underneath you without action on your part — worth knowing when something breaks with no obvious cause.
- The bridged MAC means it will *not* appear as its own switch port in UniFi. Don't go looking for one.

## Open

- [x] Confirm which physical machine hosts the hypervisor — NUC8i7BEH at `192.168.1.10`, confirmed 2026-08-11
- [x] Confirm install method — **HAOS VM**, confirmed 2026-08-11
- [ ] Enable HA's built-in scheduled backup, target [[Synology NAS]] — highest value, lowest effort item here
- [ ] Add this VM to a `vzdump` set on [[Proxmox]]
- [ ] Record integrations + controlled devices

## Related

- [[Proxmox]] · [[Home Lab]] · [[Self-Hosted Software]] · [[Hermes Agent]] · [[Backups]] · [[Network Stack]]

## Log

- 2026-08-11 — **Confirmed running.** Was written the same day as an open question ("not confirmed running anywhere"); resolved within hours by a UniFi client screenshot showing `homeassistant` at `192.168.1.169` on USW 24 PoE port 20. Mac confirmed it runs in Proxmox. Rewritten from open question to article.
