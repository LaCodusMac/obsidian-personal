---
title: "Hardware Inventory"
aliases: [Hardware]
type: resource
tags: [resource, homelab, hardware]
confidence: "partly from network doc (not fully current) + user-listed items"
---

Physical equipment in the [[Home Lab]] — from the UniFi stack to the 3D printer. Compute/NAS rows are from the [[Network Stack]] doc (not fully current); verify specs and add IPs.

## Network
- **UniFi Gateway / Router** — routing, VLANs, firewall, VPN (WireGuard/Teleport).
- **UniFi Switch** — LAN.
- **UniFi AP(s)** — Wi-Fi, SSIDs, guest network.
- **[[UniFi Cloud Key]]** — runs the UniFi Network Controller (confirmed). Not on [[NUC10]].
- **[[Raspberry Pi 5]] ×3** — CanaKit kits. `Pi-hole-1` (`192.168.1.18`, static) runs [[Pi-hole]] (LAN DNS); two spare, one earmarked for `Pi-hole-2`.

## Compute
- **Lenovo P3 Mini** — runs [[Hermes Agent]] as a Linux desktop instance. This is the agent host (confirmed).
- **Gaming PC** — runs [[Prusa Mini]] print control (PrusaLink/PrusaConnect); also general gaming. ⚠️ Fill in specs + OS.
- **[[NUC10]]** — confirmed main app host (30 GiB RAM / 233 GB NVMe, Ubuntu 25.04 + Docker), hostname `server`. Doc had the model wrong (FNH vs. actual FNK) and undersold the role — runs Plex plus the full *arr stack and a Prometheus/Grafana monitoring stack, not just Plex.
- **Intel NUC8i7BEH** — **confirmed [[Proxmox]] host at `192.168.1.10`**, on USW 24 PoE port 20, running the [[Home Assistant]] HAOS VM (2026-08-11). Was listed here for months as just "secondary utility / lab node" with nothing recorded against it. Specs, Proxmox version, and storage layout still unrecorded; UniFi reports the hostname as `DESKTOP-G3JQ8MO`, likely a stale Windows-era lease.
- **OptiPlex Micro** — optional VM / lab node.
- **Backup Laptop** — backup/DR helper.
- **Torrent Laptop** — isolated media intake/downloader.

## Storage
- **Synology NAS** — central storage + backup target (DSM, SMB/NFS, snapshots).

## Peripherals
- **[[Prusa Mini]]** — 3D printer, connected to the **gaming PC** (not the lab NUCs). See its note for details.

## Spare / repurpose candidates (from doc)
- **HP EliteDesk SFF** — DIY NAS candidate (TrueNAS Scale / OMV).
- **Dell Inspiron** — low-priority backup/utility host.
- **Lenovo ThinkCentre** — general lab node / small VM box. The "(Proxmox)" label this row used to carry came from the old network doc as a *plan*. [[Proxmox]] is now confirmed to exist somewhere in the lab, but there is no evidence it's this machine — don't let the label become the answer by default.

## To capture per device
Hostname · static IP · OS · role · what it currently runs · power/notes.

## Related
- Area: [[Home Lab]]
- Resources: [[Network Stack]], [[Self-Hosted Software]]
