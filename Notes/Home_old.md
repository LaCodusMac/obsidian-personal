---
title: Home
type: hub
updated: 2026-07-28
---

# 🧠 Jacob Vault

Central hub. Everything worth knowing branches out from here.

## 📁 Active Projects
```dataview
TABLE status, priority, updated AS "Last Updated"
FROM "01-Projects"
WHERE status != "archived"
SORT priority DESC, updated DESC
```

## 🌐 Areas of Responsibility
```dataview
LIST
FROM "03-Areas"
```

## 🕓 Recently Touched (anything, anywhere)
```dataview
TABLE file.mtime AS "Last Edited"
FROM "01-Projects" OR "02-People" OR "03-Areas" OR "04-Resources"
SORT file.mtime DESC
LIMIT 10
```

## ⚠️ Stale Projects (no update in 30+ days)
```dataview
TABLE updated
FROM "01-Projects"
WHERE status != "archived" AND date(updated) < date(today) - dur(30 days)
SORT updated ASC
```

## 📚 Resources
```dataview
LIST
FROM "04-Resources"
```

## 🗃️ Archive
```dataview
LIST
FROM "05-Archive"
```

## 🚨 Top Risk
**Nothing is backed up.** Hermes memory, KalshiWatch DB, and this vault all live on single machines with no backup job. Full plan now exists in the **[[Backups]]** area (reusable restic/systemd pattern + a note per service). Fix in setup order, [[Backup — Hermes]] first.

## 📥 To Document / To Do
- [ ] **Set up backups** — full plan in [[Backups]]; start with [[Backup — Hermes]]
- [x] Hermes host → Lenovo P3 Mini; KalshiWatch runs there too
- [x] 3D printer → [[Prusa Mini]] on gaming PC
- [x] Family instances → one Hermes agent, separate Telegram processes per person
- [ ] Confirm Hermes memory is scoped per user (no bleed across me/[[Mom]]/[[Nana]]) — [[Family Bots]]
- [ ] Locate Hermes memory on disk (so the backup job can target it) — [[Hermes Agent]]
- [ ] Workout Tracker storage + commands — [[Workout Tracker]]
- [ ] Cross-link existing in-vault Kalshi docs into [[KalshiWatch]]
- [ ] Any self-hosted services not yet listed — [[Self-Hosted Software]]
- [ ] Other projects not yet captured (add them here as you think of them)

---
Maintained by you + an AI assistant. See [[AI Maintenance Guide]] for the rules it follows, and [[Changelog]] for a running log of what it's changed.
