---
title: "Raspberry Pi 5"
aliases: [Pi 5, Raspberry Pi, CanaKit, the Pis, Pi-hole host, Pi-hole-1]
type: device
tags: [homelab, hardware, dns]
---

Three Raspberry Pi 5 boards in CanaKit kits. **`Pi-hole-1` (`192.168.1.18`) runs [[Pi-hole]]** — this is where the lab's DNS filtering actually lives. The other two are spare, one of them earmarked for a second resolver.

## Current state

- Quantity: 3, all CanaKit Pi 5 kits
- Roles: 1 × Pi-hole (DNS filtering for the [[Home Lab]]), hostname `Pi-hole-1` at **static `192.168.1.18`**; 2 × spare, unassigned
- The `-1` suffix is deliberate — a second resolver (`Pi-hole-2`) is the intended use for one of the spares. Not built yet.
- Spare Pi hostnames: not yet assigned
- OS / Pi 5 model (RAM tier), storage (SD vs. NVMe HAT): ⚠️ unrecorded
- Pi-hole install method (bare-metal vs. container): ⚠️ unrecorded — matters for [[Backup — Pi-hole]]

## Depends on

- [[Network Stack]] — the Pi-hole Pi is a single point of failure for LAN DNS

## Used by

- Everything on the LAN, via DNS — see [[Self-Hosted Software]]

## Gotchas

- **Single resolver, for now.** `Pi-hole-1` is the only DNS resolver on the LAN — if it dies or is unplugged, name resolution goes with it. `Pi-hole-2` is planned (hardware is already on hand); until it exists, this remains the lab's most exposed single point of failure.
- Not backed up. Rebuilding adlists and custom DNS by hand is tedious — see [[Backup — Pi-hole]].
- SD-card wear is the classic Pi failure mode if it's booting from SD; worth confirming which.

## Spare capacity

Two unassigned Pi 5s. One is earmarked for `Pi-hole-2` as the second resolver. The other is genuinely free — moving [[Prusa Mini]] print control off the gaming PC is a use its own note already floats.

When `Pi-hole-2` gets built, the two decisions that need making: how clients find both resolvers (DHCP handing out two DNS servers via the UniFi gateway, or a shared VIP), and how adlists/custom DNS stay in sync between them (gravity-sync or equivalent) so they don't silently diverge.

## Log

- 2026-08-08 — Recorded. Confirmed Pi-hole runs here, not on NUC8/NUC10 as the [[Network Stack]] doc assumed. Pi-hole host's hostname is `Pi-hole-1`.
