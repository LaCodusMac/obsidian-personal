---
title: "Hardware Inventory"
type: resource
tags: [resource, homelab, hardware]
confidence: "partly from network doc (not fully current) + user-listed items"
related_areas: ["[[Home Lab]]"]
related_resources: ["[[Network Stack]]", "[[Self-Hosted Software]]"]
---

# Hardware Inventory

Physical equipment in the [[Home Lab]] — from the UniFi stack to the 3D printer. Compute/NAS rows are from the [[Network Stack]] doc (not fully current); verify specs and add IPs.

## Network
- **UniFi Gateway / Router** — routing, VLANs, firewall, VPN (WireGuard/Teleport).
- **UniFi Switch** — LAN.
- **UniFi AP(s)** — Wi-Fi, SSIDs, guest network.

## Compute
- **Lenovo P3 Mini** — runs [[Hermes Agent]] as a Linux desktop instance. This is the agent host (confirmed).
- **Gaming PC** — runs [[Prusa Mini]] print control (PrusaLink/PrusaConnect); also general gaming. ⚠️ Fill in specs + OS.
- **Intel NUC10i5FNH** — documented main app host (32 GB / 250 GB SSD, Ubuntu + Docker + Plex). *Verify what actually runs here now that Hermes is on the P3 Mini.*
- **Intel NUC8i7BEH** — secondary utility / lab node.
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
- **Lenovo ThinkCentre** — general lab node / small VM box (Proxmox).

## To capture per device
Hostname · static IP · OS · role · what it currently runs · power/notes.

## Related
- Area: [[Home Lab]]
- Resources: [[Network Stack]], [[Self-Hosted Software]]
