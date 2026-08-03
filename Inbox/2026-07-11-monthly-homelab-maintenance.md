---
date: 2026-07-11
source: chatgpt
title: "Monthly Homelab Maintenance"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Every month, make a practical home lab maintenance checklist for my UniFi network, Synology NAS, Pi-hole/Unbound, UPS, rack temperature, and Plex/media services, flagging updates, backups, drive health, power, and alert checks.

**ChatGPT:** Before I set this up, I need a couple of details so the monthly checklist arrives the way you want.

genui{"ask_user_input":{"questions":[{"question":"When should I send your monthly home lab maintenance checklist?","options":["1st of the month","First Saturday","Last day of the month","Custom"],"type":"single_select","free_text_placeholder":"Enter a different day or time"},{"question":"What should be included every month?","options":["Only maintenance checklist","Include recommended firmware/software updates","Include security review","Include capacity & performance summary"],"type":"multi_select","free_text_placeholder":"Add anything else to check"}]}}

**You:** > When should I send your monthly home lab maintenance checklist?
First Saturday

> What should be included every month?
Only maintenance checklist, Include recommended firmware/software updates, Include security review, Include capacity & performance summary

**ChatGPT:** Done! I'll send it on the **first Saturday of every month**.

Each monthly report will include:

- **UniFi:** firmware recommendations, gateway/switch/AP health, client issues, VLANs, Wi-Fi performance, and security settings to review.
- **Synology NAS:** DSM/package updates, SMART and drive health, storage pool status, volume usage, backup verification, and any warnings.
- **Pi-hole & Unbound:** blocklist updates, DNS health, cache performance, query statistics, and security checks.
- **UPS:** battery health, self-test reminders, runtime, load, and power event review.
- **Rack environment:** temperature trends, cooling/airflow checks, and any thermal concerns.
- **Plex & media services:** Plex updates, library health, storage growth, Sonarr/Radarr/Prowlarr checks, download issues, and overall service status.
- **Capacity & performance:** storage utilization, CPU/RAM trends where relevant, and recommendations before anything becomes a problem.
- **Security review:** any firmware/software that should be updated promptly, stale services, and configuration items worth reviewing.

The report will focus on **actionable maintenance** rather than being a long status dump, so you can work through it in 10–20 minutes each month.
