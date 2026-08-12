---
title: "UniFi Cloud Key"
aliases: [Cloud Key, UniFi Controller, UniFi Network Controller, CK]
type: device
tags: [homelab, hardware, network]
---

The Ubiquiti Cloud Key appliance that runs the UniFi Network Controller — the management plane for the UniFi gateway, switch, and APs in the [[Network Stack]].

## Current state

- Runs the UniFi Network Controller as a dedicated appliance (not a container, not on [[NUC10]])
- Model / generation (Cloud Key Gen2, Gen2+, or original): ⚠️ unrecorded
- IP / hostname: ⚠️ unrecorded
- Manages: UniFi Gateway/Router, UniFi Switch, UniFi AP(s) — see [[Hardware Inventory]]

## Depends on

- [[Network Stack]]

## Used by

- Network administration — VLANs, firewall rules, Wi-Fi/SSIDs, VPN config

## Gotchas

- **The `/opt/unifi` compose file on [[NUC10]] is dead weight.** A UniFi Controller config with data and logs sits there with no container running. The real controller is here, on the Cloud Key. Leaving the stale config in place invites someone (or some agent) to "helpfully" start it later and end up with two controllers fighting over the same devices. Safe to remove once you've confirmed nothing references it.
- Gen2/Gen2+ models have an internal eMMC or 2.5" drive that can fail — the controller config is worth backing up regardless. See [[Backup — UniFi]].
- Losing the controller doesn't take the network down (the gateway and APs keep forwarding on last-known config), but it does take management, stats, and config changes with it.

## Log

- 2026-08-08 — Recorded. Resolves the "UniFi Controller present at `/opt/unifi` but not running" question from the NUC10 inventory: it was never supposed to run there.
