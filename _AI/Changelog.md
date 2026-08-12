---
title: Changelog
type: meta
---

# Changelog

Append-only. Newest at top. One or two lines per session.

## 2026-08-12 — Fitness MOC and Workout Tracker filled in from live Hermes state

Both notes were stubs with "fill in" lists. Written from the actual files on disk rather than
from memory: `~/.hermes/workout-531/state.json`, the tracker workbook, and the
`wendler-531-coach` skill.

- **[[Fitness]]** now carries the program (Wendler 5/3/1, started 2026-06-06 calibration,
  Cycle 1 from 2026-06-15), the goal, current training maxes (squat 205 / bench 165 /
  deadlift 245 / OHP 115), the weekly split, and the three open training threads — knee pace
  sensitivity, deadlift grip, bodyweight on 7-day average only.
- **[[Workout Tracker]]** documents the five workbook sheets and what each column holds, the
  three-way split of concerns (skill = how to coach, `state.json` = where I am now, workbook =
  what happened), and the interface. **There are no slash commands** — it's plain conversational
  Telegram, which is worth stating explicitly since the old stub asked for a command list that
  doesn't exist. Same for reports: no Grafana, no charts, everything comes back as chat.

Noted that `~/.hermes/workout-531/` is unbacked-up and belongs in the [[Backup — Hermes]] job,
since it sits under the same directory.

Closed the "Workout Tracker storage + commands" open loop on [[Home]].

## 2026-08-11 (d) — remote inspected: no divergence, but the committed `.gitignore` is unsafe

Mac ran the fetch. [[Vault Git Reconciliation]] rewritten with measured facts in place of the
speculative "2a / 2b" branches.

**Good news:** there is **no divergence**. `HEAD` is an ancestor of `origin/main` — one commit
behind, a clean fast-forward. No parallel restructure happened on the P3. The single remote
commit is `23ca9ab "auto-sync: 2026-08-03 21:05:09"` and it touches exactly one file.

**Bad news, and it is the most consequential thing found in this vault so far:** that file is
`.gitignore`, and **the committed version contains no private-file rule.** It is 11 lines of
Obsidian / macOS / iCloud patterns. The `.gitignore` carrying `Library/*.private.md` — the one
with the reasoning comments — has only ever existed untracked on the MacBook, which is why the
auto-sync pushed the weaker one.

The exposure is not hypothetical: **the P3's hourly auto-sync timer is armed with a
`.gitignore` that protects nothing.** If that machine ever receives `Library/`, the timer
commits and pushes all 62 sensitive transcripts. [[VAULT]] §6 is explicit that git is the one
place deletion doesn't delete, and that repo visibility can change retroactively.

Neither `.gitignore` is a superset of the other — local has the private rule; remote has
`.obsidian/plugins/` and `*.icloud`. The runbook now specifies a **union**, commits it *before*
the pull, and gates the corpus commit behind
`git status --porcelain -uall | grep -i private` returning nothing.

Also verified: all 62 private files are inside `Library/`, so the path-anchored rule currently
works (0 outside). An unanchored `*.private.md` would be more robust; **proposed, not applied**
— it changes a rule documented in [[VAULT]] §6 and needs a deliberate yes.

Corrected from entry (c): the earlier note said remote state "could not be verified." It has
now been verified, and the stale-cache caveat there no longer applies.

## 2026-08-11 (c) — NUC8 identified; vault found to be 8 days uncommitted

Mac supplied the remaining unknowns. All now recorded as fact rather than flagged:

- **[[Proxmox]] host is the Intel NUC8i7BEH at `192.168.1.10`.** Closes the single largest
  blind spot in [[Hardware Inventory]] — that machine had no hostname, IP, OS, or recorded
  service since the vault was built. Propagated to `Hardware Inventory.md` and the
  `Network Stack.md` worksheet, whose "NUC8 hostname + static IP: ______" line is now filled.
  UniFi reports the hostname as `DESKTOP-G3JQ8MO`; recorded as **probably a stale
  Windows-era DHCP lease**, not the real hostname, since Proxmox is Debian. Flagged for
  `hostname -f` rather than written in as fact.
- **[[Home Assistant]] is a HAOS VM.** Rewrote the backup guidance accordingly — HAOS has a
  first-class built-in backup that restores onto any instance, which is higher value than the
  `vzdump` route because it survives replacing the hypervisor entirely.
- **[[Pi-hole]] adlists recorded**: StevenBlack unified hosts + HaGeZi `adblock/multi.txt`,
  both in the Default group. The *"Migrated from `/etc/pihole/adlists.list`"* comment dates
  this as a **v4-era install upgraded in place**, which is why `gravity.db` is the thing worth
  backing up. It does not settle the v5-vs-v6 question; `pihole -v` still needed. Added the
  aggressive-list caveat, linking the existing `2026-04-05-pi-hole-blocking-ufc-stream`
  conversation in the corpus as a probable instance of exactly that.

**New: [[Vault Git Reconciliation]]** (`runbook`). A `git status` run while verifying the
above revealed this vault has **one commit, ever** — `916aa22 "Initial vault"`, 2026-08-03 —
with 616 untracked, 626 modified, and 598 deleted files outstanding. All of `Library/`,
`VAULT.md`, `CLAUDE.md`, `People/`, `Archive/` and `Logs/` have never been committed.

The 598 deletions were audited file-by-file and are **benign**: 586 of 588 `Inbox/` deletions
match same-named files now in `Library/` (the Inbox→Library move, which git will read as
renames); the 2 unmatched are superseded staging READMEs; the other 10 are the documented
2026-08-03 renames. Nothing is lost.

Two findings worth acting on, recorded in the runbook:

1. **The 62 `.private.md` transcripts have no backup path at all.** The `.gitignore` wildcard
   is working exactly as [[VAULT]] §6 intends — verified 62 on disk, 0 tracked, 0 stageable —
   but that means committing everything will not protect them. The sensitive-material
   mechanism and the backup mechanism are the same mechanism pointed opposite ways.
2. **`.gitignore` is itself untracked.** Harmless locally, but absent from a fresh clone,
   where it would stop protecting anything. Commit it first.

Remote state could **not** be verified — the agent sandbox has no SSH keys and `git fetch`
failed on host key verification. The local `origin/main` ref matches `HEAD`, but that is a
stale cache, not evidence. Step 1 of the runbook has to be run by hand on the Mac.

## 2026-08-11 (b) — Proxmox and Home Assistant confirmed; four notes corrected

Mac supplied a UniFi client screenshot and three facts. Result: **the "no Proxmox anywhere"
claim carried by three notes was wrong**, and has been corrected everywhere it appeared.

- **[[Home Assistant]]** — rewritten from open question to article. Confirmed at
  `192.168.1.169`, hostname `homeassistant`, a VM under [[Proxmox]], bridged onto USW 24 PoE
  port 20. Its MAC (`02:ff:9d:be:23:38`) is locally-administered, which is what independently
  confirms "VM" rather than "physical box." Flagged that it has no backup coverage at all.
- **[[Proxmox]]** — existence confirmed, host still unidentified. The "three candidates"
  guesswork is dropped in favour of the actual discriminator: the hypervisor is the machine
  on **USW 24 PoE port 20**, findable from the UniFi port view without any scanning.
- **[[Pi-hole]]** — bare-metal package install and admin URL
  `https://192.168.1.18/admin/login` recorded. That URL implies **v6 (~70%)**, which would
  make [[Backup — Pi-hole]]'s paths and teleporter command wrong; both notes now carry the
  v5/v6 divergence and the one-line check (`pihole -v`).
- **[[Tailscale]]** — NAS, Cloud Key, Pi-hole and the Proxmox host confirmed *not* on the
  tailnet. Recorded the expansion decision as native-client vs. subnet-router rather than
  per-device yes/no, plus the trap where making Pi-hole the tailnet nameserver upgrades a
  LAN-scope single point of failure into a global one.

Corrected in place, each with a dated inline note rather than a silent edit:
`Network Stack.md`, `Synology NAS.md`, `NUC10.md` (all three had stated or implied no
Proxmox existed), `Hardware Inventory.md` (NUC8 marked as the leading candidate; the
ThinkCentre's inherited "(Proxmox)" label demoted to a plan, not an answer), and
`Self-Hosted Software.md` (Home Assistant moved from "still unconfirmed" to confirmed).

**Root cause worth remembering:** three notes each correctly said "no Proxmox *here*," and
that aggregated into "no Proxmox *anywhere*." An inventory's coverage and its conclusions are
different things. The NUC8 was never inventoried, and still hasn't been.

## 2026-08-11 — Five missing notes created; broken-link count now zero

Created `Notes/Pi-hole.md`, `Notes/Tailscale.md`, `Notes/Grafana.md`, `Notes/Proxmox.md`,
and `Notes/Home Assistant.md`. These five were linked from `MOCs/Homelab`,
`MOCs/Self-Hosted`, `Hardware Inventory`, `Raspberry Pi 5`, and `Self-Hosted Software` but
had no article. Curated-layer broken links went 5 → 0 (verified by rescan after writing, not
assumed). No existing file was edited, renamed, or moved.

Two of the five are deliberately **not** articles. `Proxmox.md` and `Home Assistant.md` are
written as open questions, because three vault sources independently state no Proxmox host
has been confirmed and Home Assistant appears on no enumerated host. Outside context (not
from this vault) claims both run on the Intel NUC8i7BEH — that claim is recorded in both
notes, attributed as external, and flagged unverified rather than asserted. Each note carries
the specific command that would settle it (`nmap -p 8006` / `-p 8123`) and says what should
happen to the note in either outcome.

Other unverified claims are marked inline with ⚠️ rather than stated flat: Pi-hole's install
method and DHCP advertisement, Tailscale's ACL policy and full membership, and Grafana's
possible `0.0.0.0:3001` exposure on the P3 Mini instance. `Grafana.md` keeps the two
instances (NUC10 Docker :3000 vs. `kalshi-grafana.service`) explicitly separated, per the
existing warning in `Self-Hosted Software.md` not to conflate them.

**Not done, flagged for a decision:** root `Plex.md` is a 0-byte file created 2026-08-11. It
currently captures every `[[Plex]]` link in the vault — including from `MOCs/Self-Hosted` and
`Synology NAS` — so those links resolve to an empty note. Left in place; not archived.

## 2026-08-08 — Pi-hole host recorded: `Pi-hole-1` at static 192.168.1.18

Recorded across `Raspberry Pi 5.md` (+ hostname added as an alias), `Network Stack.md`
(diagram, corrections, worksheet — the worksheet's Pi-hole line is now filled, not blank),
`Hardware Inventory.md`, `Self-Hosted Software.md`, and `Backup — Pi-hole.md`.

The `-1` suffix was forward-looking per Mac: `Pi-hole-2` on one of the two spare Pi 5s is
the intent, not yet built. Recorded as **planned**, and the single-resolver gotcha reworded
to reflect that rather than reading as an unconsidered gap. Added the two open decisions a
second resolver will force (how clients learn both addresses; how adlists stay in sync).

## 2026-08-08 — Pi-hole and UniFi controller hosts confirmed; two new device notes

Mac answered the two open questions from the NUC10 inventory earlier today. New
`Notes/Raspberry Pi 5.md` (3× CanaKit Pi 5; **one runs Pi-hole**, two spare) and
`Notes/UniFi Cloud Key.md` (runs the UniFi Network Controller as an appliance). Both were
guesses in the `Network Stack` doc — it put DNS on "NUC8 or UniFi-integrated fallback" and
left the controller unplaced.

Propagated to `Network Stack.md` (topology diagram + corrections + worksheet),
`Hardware Inventory.md`, `Self-Hosted Software.md`, `NUC10.md`, `Backup — Pi-hole.md`
(host was "NUC8 or wherever Pi-hole runs"), and `Backup — UniFi.md`. The `/opt/unifi`
compose file on NUC10 is now documented as a stale leftover with a don't-start-it warning,
rather than an open question.

Two things flagged in the new notes rather than silently recorded: single Pi-hole = LAN-wide
DNS single point of failure, with two idle Pi 5s available as the obvious fix; and hostnames
/IPs for both new devices are still unrecorded.

`kalshi-demo.pem` gotcha in `NUC10.md` updated — permissions locked down per Mac; kept the
note that it's a stray copy on a host that doesn't use it, rather than deleting the entry.

## 2026-08-08 — NUC10 full inventory; corrected Network Stack/Synology/Self-Hosted Software

New `Notes/NUC10.md` (`type: device`) from a live shell inventory Mac ran on the machine
(hostname `server`, Intel NUC10i5FNK). Corrects several unconfirmed assumptions the
[[Network Stack]] doc had been carrying: model number (FNH → FNK), that it runs *only* Plex
(it also runs the full *arr stack + Prometheus/Grafana/node-exporter), that qBittorrent lives
on a separate torrent laptop (it's a container on NUC10 via gluetun), and that NAS shares
export to Proxmox (they export to NUC10 directly — no Proxmox confirmed anywhere in the lab
yet). Also flagged as open questions: Pi-hole/AdGuard wasn't found on this host, so its
location is unconfirmed; UniFi Controller config exists at `/opt/unifi` but isn't running.
Updated `Hardware Inventory.md`, `Network Stack.md`, `Synology NAS.md`,
`Self-Hosted Software.md`, and `Backup — Plex.md`'s host field to match.

**Flagged, not fixed:** `kalshi-demo.pem` sits loose and unencrypted in `/home/ubuntu` on
NUC10, unrelated to any service that actually runs there ([[KalshiWatch]] runs on the P3
Mini). Noted as a gotcha in `NUC10.md`; told Mac directly it's worth securing/removing if
live. Did not touch the file or move/inspect its contents.

## 2026-08-08 — Added Plex Storage Recovery runbook

New `Notes/Plex Storage Recovery.md` (`type: runbook`): the check/fix commands for
remounting Synology media after a power outage or reboot (script-based and manual paths),
sourced from Mac's own instructions. Linked from `Synology NAS.md`'s existing gotcha line.
No new stubs created — `[[Plex]]` remains an intentional stub per the 2026-08-03 list.

## 2026-08-03 — 61 sensitive conversations imported; C2, D2, D5 resolved

### The import, and a near-miss
Mac dropped the 61 sensitive files into **`_AI/Private/<Category>/`** — a path
`.gitignore` does not match. Git had all 61 staged as untracked and would have committed
them on the next `git add .`. Caught on the first scan. This is precisely the failure mode
`VAULT.md` §6 describes: the protection is the `.private.md` suffix, and a sensitive file
without it looks entirely normal.

- Moved all 61 → `Library/` flat as `<slug>.private.md`; `status:` stripped to match.
- Verified with `git check-ignore` per file: 61/61 ignored, 0 sensitive paths in
  `git status`, 0 staged in a simulated `git add`.
- Removed the now-empty `_AI/Private/` tree.
- `Private Index.private.md` generated (61 entries, itself gitignored).
- Library now 649 files: 584 public + 61 private + 4 meta.

**Deliberately treated all 61 as sensitive without triage.** The heuristic clearly
over-fired — a cheese review, a Korean War overview, and an SSD troubleshooting thread are
in the set, alongside genuinely private health, financial, and relationship material. But
the error costs are asymmetric: wrongly private is free and reversible, wrongly public is
permanent once pushed. Reclassification is a follow-up, not a blocker.

### Also done
- **Lead sentences (C2) applied to all 29 curated notes.** Most already had a good sentence
  sitting *after* the H1 or under a `## Summary` heading — hoisted rather than rewritten, so
  the wording is Mac's. Only `Network Stack` needed one written. Redundant H1s removed
  (`title:` and the filename already show it). 0 violations remain.
- **Aliases (D5) added** — 16 across 11 notes (`Hermes`, `Kalshi`, `Prusa`, `The Lab`, …).
  Script aborts if an alias collides with an existing filename or another alias; `Homelab`,
  `Self-Hosted`, and `Vault` were rejected on those grounds since `MOCs/Homelab.md`,
  `MOCs/Self-Hosted.md`, and `VAULT.md` already own them.
- **`Logs/` kept and documented** (`Logs/About Logs.md`) rather than dropped. It's queried by
  `Home.md`, three MOCs, and the MOC template. Also: git doesn't track empty directories, so
  an empty `Logs/` would have vanished on a fresh clone.
- **The six broken links are confirmed intentional stubs** (D2) — `Proxmox`, `Plex`,
  `Pi-hole`, `Grafana`, `Home Assistant`, `Tailscale`. Recorded in `VAULT.md` §8 so future
  audits don't re-flag them as defects.

## 2026-08-03 — canonical spec + `related_*` retired (C1, C5, D4 resolved)

Consolidated the vault's rules into one file so they can't contradict each other again.

- **New `VAULT.md`** — canonical spec: structure, frontmatter schema, writing conventions,
  import workflow, sensitive handling, maintenance. Everything else defers to it.
- **New `CLAUDE.md`** at root — loaded automatically by Claude Code / Cowork sessions, so
  the rules apply without anyone remembering to point an agent at them.
- `README.md` reduced to human setup + a pointer. `_AI/AI Maintenance Guide.md` reduced to
  assistant-specific behaviour (verify before reporting, don't destroy information while
  applying a rule, log accurately) — its structural rules now live in `VAULT.md` only.
- **`related_*` stripped** — 54 lines across 22 files. **Four notes had relationships that
  existed only in frontmatter** (`Backup — Plex`, `Backup — Synology Config`,
  `Backup — UniFi`, `Obsidian Brain`); those 7 links were written into the bodies first.
  Stripping blind would have silently lost them.
- **`updated:` stripped** from 6 files — banned by the same rule, also never applied.
- **Type vocabulary fixed.** Three competing lists were in play: `README` said
  `device|service|concept|area|howto`, templates used `device|log|moc|runbook`, real notes
  used nine other values. `VAULT.md` §3 now defines one 12-value list from actual usage.
- **Templates consolidated** into `Templates/` — `Person Template.md` and
  `Project Template.md` moved out of `Notes/` (they were orphaned articles in the article
  namespace), `Log_Entry.md` → `Log Entry.md` for the spaces-not-underscores rule.
- **`Notes/README.md` archived** → `Archive/Notes README (PARA era).md`. It still described
  `01-Projects/`, `02-People/` etc. and the `related_*` model. Also resolves the
  three-files-named-README ambiguity.
- **`Notes/Obsidian Brain.md` rewritten** — described the vault as PARA with `related_*` as
  the current linking model.
- Self-inflicted and fixed: the edit to `Templates/Project.md` introduced an unbacktciked
  `[[wikilinks]]`, caught on the verification pass.

## 2026-08-03 — sensitive-conversation boundary (B2 resolved)

The 61 sensitive conversations exist after all; Mac has them. They were never in this
vault, not deleted from it. Prepared the boundary before importing.

- **Decision:** sensitive notes live flat in `Library/` like everything else — fully
  searchable, agent-readable, Obsidian-synced — but are **excluded from git**. The repo
  (`LaCodusMac/obsidian-personal`) is private, but git history is the one place where
  deleting later doesn't delete, and repo visibility can change retroactively.
- **Mechanism:** filename suffix `.private.md`, matched by one wildcard in `.gitignore`.
- Rejected: listing the 61 filenames in `.gitignore` — that file is committed, and the
  slugs describe their contents, so it would publish what it's meant to hide.
- Rejected: `.git/info/exclude` — never committed, so protection vanishes on a fresh
  clone. Silent failure is worse than none.
- **`Conversation Index.md` split.** Same leak: the index is committed and lists
  filenames. Sensitive notes now go to `Private Index.private.md`, itself gitignored.
- Added `_AI/regenerate_index.py`: regenerates both indexes from frontmatter and fails
  loudly on `sensitive: true` without the suffix, suffix without the flag, unknown
  category, or any sensitive file git isn't actually ignoring. Verified against
  simulated good and bad files.
- Also added `.gitignore` coverage for `.obsidian/workspace.json`, `.trash/`, `.DS_Store`.
- **Not protected:** nothing is encrypted. Anyone with vault or Obsidian Sync access
  reads these in plaintext — by design, since agents must be able to. The boundary is
  "not in a remote git repo," not "secret."

## 2026-08-03 — Inbox doctrine reversed (B1 resolved)

**Decision: the corpus is a permanent, model-agnostic memory store, not disposable
quarantine.** The `Import Schema.md` philosophy wins; the "mine and delete" doctrine is
retired. Rationale: no single provider should hold the only copy of that context.

- `Inbox/` → **`Library/`**. 584 conversations, flat, permanent.
- Layout: flat with `category` in frontmatter, *not* the `Library/<Category>/` +
  `Library/Private/` tree the schema originally specified. Category folders would
  duplicate what frontmatter already carries, and flat matches `Notes/`.
- **`status:` removed from all 584 files.** A flag you must remember to flip is a queue
  that never drains — that critique survived the philosophy change. Membership in a
  library isn't conditional on review.
- **`Library/Private/` formally dropped.** The 61 sensitive conversations the old index
  referenced were never in this vault (no trace in git; single initial commit). Counts
  corrected 645 → 584. `sensitive:` survives as an advisory field for pre-share skimming.
- `Conversation Index.md` regenerated from frontmatter — now reproducible rather than
  hand-maintained. Checkboxes removed with the review queue.
- Deleted `Inbox/README.md` (was the quarantine doctrine) and `Inbox/Staging_README.md`
  (staging folder never existed; unset `category` is a better unfiled signal).
  Replaced by `Library/About the Library.md`.
- Docs rewritten to match: root `README.md` (structure, setup step 2, rule 3),
  `_AI/AI Maintenance Guide.md` (rule 7 append-only, new rule 6b "use Library before
  answering"), `Home.md` (Library section), `Notes/Portable Context Pack.md` (gotcha).
- **Reversal worth noting:** the audit's A3 said to exclude the corpus from search. That
  was premised on the quarantine model and is now wrong — README step 2 says the
  opposite. A memory store you can't search isn't one.

## 2026-08-03 — audit + mechanical fixes
- Full read-only audit written to `_AI/Vault_Audit_2026-08-03.md`. Nothing else was
  changed without approval; the items below were approved individually.
- Renamed three files from underscores to spaces so wikilinks resolve:
  `AI_Maintenance_Guide` → `AI Maintenance Guide`, `Synology_NAS` → `Synology NAS`,
  `Portable_Context_Pack` → `Portable Context Pack`. Fixed 6 broken links, including
  `Home.md`'s own footer link to the maintenance guide.
- Moved `Mom.md` and `Nana.md` from `Notes/` to `People/` (rule 6). Wikilinks
  unaffected — Obsidian resolves by filename, not path.
- Archived `Notes/Home_old.md` → `Archive/Home_old.md` with a dated reason (rule 7).
  This also removed 8 of the 9 Dataview queries pointing at the dead PARA folders.
- `Notes/Backups.md`: repointed its status table from `FROM "04-Resources"` (folder
  does not exist) to `FROM "Notes"`. Was silently returning nothing.

### Correction to the 2026-07-31 entry below
`related_*` frontmatter was **not** actually dropped — 22 files still carry
`related_areas` / `related_resources` / `related_projects`, including both templates
in `Notes/`. The entry below overstated what happened. Left in place pending a
decision on whether to strip the fields or amend rule 4.

## 2026-07-31
- Vault restructured: flat `Notes/` article namespace, `MOCs/` entry points,
  `Logs/` for dated entries, `Inbox/` quarantine for raw AI transcripts.
- Dropped `related_*` frontmatter fields (dual maintenance) and hand-written
  `updated:` (use `file.mtime`).  ← see correction above; not done.
- Kalshi moved out to its own vault inside the code repo.
