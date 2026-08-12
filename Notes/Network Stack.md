---
title: "Network Stack"
aliases: [Network, Topology]
type: resource
tags: [resource, homelab, network, documentation]
source: "home_network_software_stack.pdf (self-authored)"
confidence: "not fully up to date — do not treat as bible"
---

The documented topology of the home network — what routes, what switches, and where each service sits. Derived from my own PDF and **not confirmed against live config**.

> ⚠️ **From my own documentation PDF, explicitly not fully current.** Roles below are the documented/recommended layout, not confirmed live config. Where the doc used assumptions, they're marked. Verify before relying on any of it.

## Topology (as documented)
```
Internet / ISP
  └─ UniFi Gateway / Router
       ├─ UniFi Switch / LAN
       │    ├─ UniFi Cloud Key — Network Controller appliance (confirmed 2026-08-08)
       │    ├─ Raspberry Pi 5 ×3 — `Pi-hole-1` (192.168.1.18) runs Pi-hole (LAN DNS), two spare (confirmed 2026-08-08)
       │    ├─ Synology NAS (DSM, SMB/NFS, snapshots, backup target)
       │    ├─ Intel NUC10i5FNH — main app host (Ubuntu Server + Docker + Plex)
       │    ├─ Intel NUC8i7BEH — secondary node (lab / utility / test)
       │    ├─ Backup Laptop — replication / cold standby / file sync
       │    ├─ Torrent Laptop — isolated downloader / media intake
       │    ├─ OptiPlex Micro — optional VM / lab node
       │    ├─ Main personal laptop/desktop
       │    └─ Work laptop(s)
       └─ UniFi AP(s) / Wi-Fi → phones, tablets, TV, streaming clients
```

## Known corrections since the doc
- **[[Hermes Agent]] and [[KalshiWatch]] both run on the Lenovo P3 Mini**, not the NUC10 the doc assumes as "main app host."
- **[[NUC10]] is confirmed live** (hostname `server`, `192.168.1.29`) and does run Plex/Docker as the doc assumed — but the doc undersold it: it's also running the full *arr stack (Sonarr/Radarr/Prowlarr/qBittorrent-via-gluetun) and a Prometheus/Grafana/node-exporter monitoring stack. Model number was wrong in the doc (NUC10i5FNH vs. the actual FNK).
- **No Proxmox found on NUC10** — it's bare Ubuntu 25.04 + Docker, no hypervisor; [[Synology NAS]]'s exports go to NUC10 directly, not to Proxmox. **Update 2026-08-11:** [[Proxmox]] *does* exist elsewhere in the lab — it hosts the [[Home Assistant]] VM (`192.168.1.169`). The host machine is on **USW 24 PoE port 20**, still unidentified. This line previously read as though no Proxmox existed anywhere; it only ever meant "not on NUC10."
- **Pi-hole runs on a [[Raspberry Pi 5]]**, not NUC8 or a UniFi-integrated fallback as the doc suggested. One of three CanaKit Pi 5s; the other two are spare. Single resolver — no redundancy yet.
- **The UniFi Network Controller lives on the [[UniFi Cloud Key]]**, a dedicated appliance. The `/opt/unifi` compose file on [[NUC10]] is a stale leftover, not a second controller.
- **[[Prusa Mini]] is on the gaming PC**, not the lab infrastructure.
- **No backups are currently running** despite the doc's 3-2-1 recommendation — see [[Home Lab]].

## Documented assumptions (flagged in the source)
- NUC10i5FNH = 32 GB RAM / 250 GB SSD, main Ubuntu/Docker host. **Confirmed close but not exact** — actual unit is an FNK with 30 GiB RAM / 233 GB NVMe; see [[NUC10]].
- NUC8i7BEH = secondary node.
- Synology = shared media + backup storage.
- UniFi handles routing/VPN/Wi-Fi.
- Exact models/IPs were **not confirmed** in the doc — recommended roles used instead.

## Suggested service placement (as documented)
- **Plex** → NUC10 (compute), libraries pointed at Synology over NFS.
- **Media storage** → Synology (dedicated movies/tv shares).
- **DNS filtering (Pi-hole/AGH)** → NUC8 or UniFi-integrated fallback; 2nd resolver later for redundancy. *(Actual: `Pi-hole-1` on a [[Raspberry Pi 5]]. The 2nd resolver is planned — `Pi-hole-2` on a spare Pi — not yet built.)*
- **VPN** → UniFi Gateway (WireGuard/Teleport), admin interfaces off the open internet.
- **Backups** → Synology + backup laptop (3-2-1 logic).
- **Download automation** → Torrent laptop (isolated), move completed media off-box.
- **Monitoring/uptime** → NUC8 or OptiPlex (Uptime Kuma, Grafana, node_exporter).

## Fill-in worksheet (finalize live values)
- Gateway / UniFi controller hostname: controller runs on the [[UniFi Cloud Key]]; hostname/IP still ______
- Pi-hole host + IP: `Pi-hole-1` — static `192.168.1.18`, a [[Raspberry Pi 5]]
- LAN subnet(s) / VLAN IDs: 192.168.1.0/24 confirmed (NUC10 side); VLAN IDs still unknown
- Synology hostname + static IP: `192.168.1.82` (hostname unconfirmed)
- NUC10 hostname + static IP: `server` — `192.168.1.29` (also on Tailscale at `100.121.218.72`) — see [[NUC10]]
- NUC8 hostname + static IP: **`192.168.1.10`** — runs [[Proxmox]], hosting the [[Home Assistant]] HAOS VM. Confirmed 2026-08-11. Hostname reported by UniFi as `DESKTOP-G3JQ8MO`, probably a stale Windows-era DHCP lease rather than the real one — verify with `hostname -f`. Addressing is a **UniFi DHCP reservation**, not a host-side static — confirmed 2026-08-11.
- Backup laptop / Torrent laptop hostnames + IPs: ______
- Plex claim / URL / port: ______
- NFS export path(s) from Synology: ______
- Primary backup job(s): ______
- VPN method + admin access rule: ______
- Off-site / secondary backup location: ______

## Related
- Area: [[Home Lab]]
- Resources: [[Hardware Inventory]], [[Self-Hosted Software]]
