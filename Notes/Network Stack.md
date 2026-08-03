---
title: "Network Stack"
type: resource
tags: [resource, homelab, network, documentation]
source: "home_network_software_stack.pdf (self-authored)"
confidence: "not fully up to date — do not treat as bible"
related_areas: ["[[Home Lab]]"]
related_resources: ["[[Hardware Inventory]]", "[[Self-Hosted Software]]"]
---

# Network Stack

> ⚠️ **From my own documentation PDF, explicitly not fully current.** Roles below are the documented/recommended layout, not confirmed live config. Where the doc used assumptions, they're marked. Verify before relying on any of it.

## Topology (as documented)
```
Internet / ISP
  └─ UniFi Gateway / Router
       ├─ UniFi Switch / LAN
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
- **[[Hermes Agent]] and [[KalshiWatch]] both run on the Lenovo P3 Mini**, not the NUC10 the doc assumes as "main app host." Re-confirm what the NUC10 actually serves now (Plex/Docker per the doc?).
- **[[Prusa Mini]] is on the gaming PC**, not the lab infrastructure.
- **No backups are currently running** despite the doc's 3-2-1 recommendation — see [[Home Lab]].

## Documented assumptions (flagged in the source)
- NUC10i5FNH = 32 GB RAM / 250 GB SSD, main Ubuntu/Docker host.
- NUC8i7BEH = secondary node.
- Synology = shared media + backup storage.
- UniFi handles routing/VPN/Wi-Fi.
- Exact models/IPs were **not confirmed** in the doc — recommended roles used instead.

## Suggested service placement (as documented)
- **Plex** → NUC10 (compute), libraries pointed at Synology over NFS.
- **Media storage** → Synology (dedicated movies/tv shares).
- **DNS filtering (Pi-hole/AGH)** → NUC8 or UniFi-integrated fallback; 2nd resolver later for redundancy.
- **VPN** → UniFi Gateway (WireGuard/Teleport), admin interfaces off the open internet.
- **Backups** → Synology + backup laptop (3-2-1 logic).
- **Download automation** → Torrent laptop (isolated), move completed media off-box.
- **Monitoring/uptime** → NUC8 or OptiPlex (Uptime Kuma, Grafana, node_exporter).

## Fill-in worksheet (finalize live values)
- Gateway / UniFi controller hostname: ______
- LAN subnet(s) / VLAN IDs: ______
- Synology hostname + static IP: ______
- NUC10 hostname + static IP: ______
- NUC8 hostname + static IP: ______
- Backup laptop / Torrent laptop hostnames + IPs: ______
- Plex claim / URL / port: ______
- NFS export path(s) from Synology: ______
- Primary backup job(s): ______
- VPN method + admin access rule: ______
- Off-site / secondary backup location: ______

## Related
- Area: [[Home Lab]]
- Resources: [[Hardware Inventory]], [[Self-Hosted Software]]
