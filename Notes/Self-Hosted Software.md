---
title: "Self-Hosted Software"
type: resource
tags: [resource, homelab, software, selfhosted]
related_areas: ["[[Home Lab]]"]
related_projects: ["[[Hermes Agent]]", "[[KalshiWatch]]"]
related_resources: ["[[Hardware Inventory]]", "[[Network Stack]]"]
---

# Self-Hosted Software

Everything I have running on the [[Home Lab]] — from Pi-hole to Plex. Confirmed items first, doc-suggested items flagged.

## Confirmed running
- **Plex** — media server.
- **Pi-hole** — network ad/DNS filtering. *(Or AdGuard Home — confirm which.)*
- **[[Hermes Agent]] + [[KalshiWatch]]** — Telegram agent and trading/monitoring stack (systemd services; see [[KalshiWatch]] for the unit list).
- **Grafana** — dashboards (`kalshi-grafana.service` for KalshiWatch; possibly shared for lab monitoring).

## From the [[Network Stack]] doc (suggested / verify)
- **Docker + Compose** on NUC10 (Portainer optional).
- **qBittorrent + VPN** on the torrent laptop; optional Sonarr / Radarr / Prowlarr.
- **Backups**: rsync / restic / Duplicati; Synology Hyper Backup.
- **Monitoring/uptime**: Uptime Kuma, node_exporter, Grafana.

## To capture per service
Host it runs on · container vs bare · port · config/data location · backup status · depends-on.

## ⚠️ Likely running but not yet listed
Add anything else here as you remember it — reverse proxy (Nginx Proxy Manager / Traefik / Caddy)? Home Assistant? Vaultwarden? Nextcloud? Watchtower? This is the "stuff I may not even be thinking about" catch-all for software.

## Related
- Area: [[Home Lab]]
- Projects: [[Hermes Agent]], [[KalshiWatch]]
- Resources: [[Hardware Inventory]], [[Network Stack]]
