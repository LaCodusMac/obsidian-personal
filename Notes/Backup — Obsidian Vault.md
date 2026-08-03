---
title: "Backup — Obsidian Vault"
type: resource
tags: [resource, backup-task, backups]
status: not-started
priority: high
host: "wherever the vault lives"
related_projects: ["[[Obsidian Brain]]"]
related_areas: ["[[Backups]]"]
---

# Backup — Obsidian Vault

This wiki ([[Obsidian Brain]]) is itself worth protecting — it's the map of everything else.

## Best option: git
A vault is just markdown, so version it. This gives history + off-site in one move:
```bash
cd /path/to/Jacob-Vault
git init && printf '.obsidian/workspace*\n.trash/\n' > .gitignore
git add . && git commit -m "snapshot"
git remote add origin <private repo, e.g. self-hosted Gitea on the lab or a private GitHub>
git push -u origin main
```
Then either commit manually or a tiny timer that does `git add -A && git commit -m "auto $(date -I)" && git push` daily.

## Or: restic (if you'd rather not use git)
Fill into the [[Backups]] pattern with `<name>=vault`, `<PATHS>=/path/to/Jacob-Vault`, exclude `.obsidian/workspace*`.

## Restore test
Clone the repo (or restic-restore) to a temp dir, open it as a vault in Obsidian, confirm notes + links load.

## Status
- [ ] Pick git vs restic
- [ ] Set up remote / repo
- [ ] Automate daily
- [ ] Test-restore
