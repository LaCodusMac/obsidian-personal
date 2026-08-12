---
title: Vault Audit — 2026-08-03
type: meta
---

# Vault Audit — 2026-08-03

629 markdown files reviewed structurally; the 584 Inbox transcripts were surveyed by
metadata, not read (see "What I did not check").

> **Status, 2026-08-03:** originally written as a read-only audit. Items A2, C3, C4 and
> D1 were subsequently approved and applied — see `Changelog.md`. Everything else below
> is still a proposal. Three findings in the original draft were wrong and are corrected
> in place, marked **CORRECTED**.

The vault's *specs* are good. The gap is that most of them were never implemented, and
two of them contradict each other.

---

## A. Functional breakage — fix first, all cheap

### A1. Dataview is not installed. `Home.md` does nothing.
`.obsidian/community-plugins.json` does not exist; no community plugins are installed.
Every query block in `Home.md` renders as a raw code fence. Your dashboard — Areas,
Recently touched, Stale, Orphans, Inbox queue — displays literally nothing.

This is the top item because the entire navigation model ("navigation by links and MOCs")
assumes that dashboard works. README lists Dataview as **required**; the step was skipped.

Templater is also absent (README lists it as optional).

### A2. Nine Dataview queries point at folders that don't exist. ✅ RESOLVED — **CORRECTED**
> **Correction:** the original draft implied nine live breakages. In fact **eight of the
> nine were inside `Notes/Home_old.md`**, the superseded file already slated for
> archiving under C4. Only one was in a live note. A2 was mostly a duplicate of C4, and
> the severity was overstated.
>
> **Applied:** `Home_old.md` archived (taking 8 queries with it); `Notes/Backups.md`
> repointed from `FROM "04-Resources"` to `FROM "Notes"`. Zero dead-folder queries
> remain in live notes.

Leftover from an earlier PARA layout. Even after installing Dataview, these return empty
forever — and fail *silently*, which is the exact failure Guide rule 4 warns about:

| Folder referenced | Query count | Exists? |
|---|---|---|
| `01-Projects` | 3 | no |
| `04-Resources` | 3 | no |
| `03-Areas` | 2 | no |
| `02-People` | 1 | no |
| `05-Archive` | 1 | no |

Notably `Notes/Backups.md` has a status table pulling `FROM "04-Resources"` — your backup
task tracker is a table that will always be blank, on the one project flagged as most
urgent in Home's open loops.

### A3. Inbox is not excluded from search.
`.obsidian/app.json` is `{}` — `userIgnoreFilters` was never set. README setup step 2 was
skipped.

This matters more than it sounds. 584 transcripts (5.5 MB) are currently in every search
result and quick-switcher lookup. Rule 1 is "search before you create," and rule 1 is what
prevents duplicate articles — the stated primary failure mode. Right now searching is
unpleasant enough that you won't do it.

---

## B. The unresolved contradiction — needs your decision

### B1. Two incompatible specs govern `Inbox/`, and neither is implemented.

**Spec 1** — root `README.md` + `_AI/AI_Maintenance_Guide.md` + `Inbox/README.md`:
> "Quarantined raw imports. Mine and delete. **Not a knowledge base.** Nothing in this
> folder should be treated as true, cited, or handed to an AI as context."

**Spec 2** — `Inbox/Import Schema.md`:
> "A growing, model-agnostic library of Jacob's AI conversations — a personal memory store
> that any AI agent can read and query, so no single provider ends up holding the only copy
> of that context."

These are opposite claims about the same 584 files: disposable staging vs. permanent
retrieval corpus. Spec 2 further specifies `Staging/`, `Library/<Category>/`, and
`Library/Private/<Category>/`.

**Actual state matches neither.** No `Staging/`, `Library/`, or `Private/` folder exists.
All 584 transcripts sit flat in `Inbox/`, all `status: pending-review`, all
`source: chatgpt`, dated 2023-03 → 2026-07, categories already assigned.

Everything else about Inbox handling depends on which spec you keep. I'd resolve this
before touching anything in that folder.

One observation, offered once: the two specs imply different *ownership* of value. Spec 1
assumes the value is in your `Notes/` articles and transcripts are slag. Spec 2 assumes the
value is in the corpus itself as agent-retrievable context. Both are defensible; the
category distribution (121 Home Lab, 99 Food, 62 Coding) suggests a real reference corpus
rather than 584 things to mine and delete. But that's your call, not an audit finding.

### B2. 61 conversations are missing, and they're the sensitive ones.
`Inbox/Conversation Index.md` header claims:
> **Total conversations:** 645 | **In this index:** 584 | **Private:** 61

584 dated transcripts exist. The 61 flagged `sensitive: true` (health / financial /
relationship_family / legal_work_conflict) are **not in the vault**, and
`Library/Private/Private Index.md` does not exist either.

Only one file in `Inbox/` contains `sensitive: true` — `Import Schema.md`, and that's the
example YAML inside the documentation, not a real flag.

So: either those 61 were deliberately withheld from this vault, or they were lost during
import. Worth confirming which — I can't tell from here, and it's the kind of thing you'd
rather know now than discover later.

---

## C. Guide violations in curated notes

### C1. `related_*` frontmatter is still everywhere. The changelog says otherwise.
Guide rule 4 bans parallel relationship fields. `_AI/Changelog.md` (2026-07-31) records:
> "Dropped `related_*` frontmatter fields (dual maintenance)"

They were not dropped. **22 files** still carry `related_areas` / `related_resources` /
`related_projects` — 20 of 26 `Notes/` files, plus both templates in `Notes/`.

The secondary problem is worse than the primary one: rule 8 makes the changelog your audit
mechanism, and the changelog is currently inaccurate. If you audit by reading it, you'll
believe a cleanup happened that didn't.

### C2. Lead-sentence rule: 26 of 26 `Notes/` files violate it.
Rule 2 — "every note opens with one plain sentence defining the thing, **before any
heading**." Every single file in `Notes/` opens with an H1. Most do have a good defining
sentence, just placed after the heading rather than before it.

Low severity, high volume. Mechanical to fix, but it's 26 judgment calls about wording, so
it's a real editing pass, not a script.

### C3. `People/`, `Logs/`, and `Archive/` are empty — but shouldn't be.
- `Notes/Mom.md` and `Notes/Nana.md` are both `type: person`. Guide rule 6: people → `People/`.
- `Logs/` is empty while `Home.md` runs four queries against it and the vault documents
  workout / print-run / sales logging as the intent.
- `Archive/` is empty while a superseded file sits in `Notes/` (see C4).

### C4. `Notes/Home_old.md` is a superseded duplicate of `Home.md`.
Still live in the article namespace. Rule 7 says move to `Archive/` with a dated line
saying why, never leave it in `Notes/`.

### C5. Templates exist in two places, and one set is wrong.
`Templates/` holds Entity, Log_Entry, MOC, Runbook. `Notes/` separately holds
`Person Template.md` and `Project Template.md` — both with `{{title}}` placeholders, both
carrying banned `related_*` fields, both orphaned. Templater isn't installed, so neither
set is actually in use.

---

## D. Link integrity

### D1. Broken links caused by underscore filenames
Obsidian resolves wikilinks by **filename or alias** — the frontmatter `title:` field does
nothing. Three files are named with underscores but linked with spaces:

| File on disk | Linked as | Broken links |
|---|---|---|
| `_AI/AI_Maintenance_Guide.md` | `[[AI Maintenance Guide]]` | 3 — incl. **`Home.md` footer** |
| `Notes/Synology_NAS.md` | `[[Synology NAS]]` | 2 — incl. `MOCs/Homelab.md` |
| `Notes/Portable_Context_Pack.md` | `[[Portable Context Pack]]` | 1 — `MOCs/AI-Stack.md` |

Two ironies worth flagging: your dashboard's own link to the maintenance guide is dead, and
README calls `Notes/Synology NAS.md` the reference example for the alias pattern — while
the file is actually named `Synology_NAS.md`, so that pointer is broken too.

Renaming the files (rather than adding aliases) fixes all six at once and matches the
spaced-filename convention the rest of `Notes/` already uses.

### D2. Links to articles that were never written
`MOCs/` and `Notes/` point at six nonexistent notes: `Proxmox`, `Plex`, `Pi-hole`,
`Grafana`, `Home Assistant`, `Tailscale`.

These may be deliberate stubs — placeholder links are a legitimate way to queue writing. But
`Self-Hosted Software.md` and `Network Stack.md` exist and cover some of this material, so
there's a real risk of writing a duplicate article later, which rule 1 exists to prevent.

### D3. ~~Accidental links from prose~~ — **WITHDRAWN, this finding was wrong**
The original draft claimed `[[wikilinks]]` was rendering as a live link in three files,
plus a malformed unclosed `[[` in `Synology_NAS.md`. **All four are inside inline code
spans** (`` `[[wikilinks]]` ``), which Obsidian does not render as links. Nothing was
broken.

Cause: my link scanner stripped fenced code blocks but not inline code spans, so it
flagged four false positives. Re-run with inline spans stripped, the real broken-link set
was six links (all D1) plus eight pointing at unwritten articles (D2) — no prose
accidents at all.

One real thing did surface while checking: `Notes/README.md` and `Notes/Obsidian
Brain.md` both describe `related_*` frontmatter as the current linking model, which
contradicts Guide rule 4. That's a documentation conflict, not a link defect — folded
into C1.

### D4. Three files named `README.md`
Root, `Inbox/`, and `Notes/`. Duplicate basenames make any `[[README]]` link resolve
ambiguously. Root `README.md` and `Notes/README.md` also overlap heavily in content
(2316 vs 2487 bytes, both describing vault setup) — likely one should be merged or archived.

### D5. Aliases are barely used
README: "aliases are **the single highest-value habit** in this vault." Only 2 of 26 notes
have any (`Synology_NAS`, `Portable_Context_Pack`). Candidates that would benefit
immediately: Hermes Agent, KalshiWatch, Prusa Mini, Pi-hole, Home Lab.

### D6. Git — **CORRECTED**
One commit (`916aa22 Initial vault`), and `.obsidian/` is untracked.

> **Correction:** the original draft said git was your only copy. Wrong — `sync: true`
> is set in `.obsidian/core-plugins.json`, so Obsidian Sync is enabled. The vault is not
> unprotected. `Backup — Obsidian Vault` is still unstarted, and Sync is replication
> rather than versioned backup (a bad edit propagates), so the restic job is still worth
> doing — but the urgency is lower than stated.

---

## Suggested order

Cheap and mechanical, no decisions needed:

1. ~~Install Dataview (A1)~~ — **still open**, needs the Obsidian UI. See the Bases note below.
2. ~~Add `Inbox` to excluded files (A3)~~ — **still open**, needs Obsidian quit first (Sync will clobber a write to `app.json` while it's running)
3. ✅ Rename the three underscore files (D1) — fixed 6 broken links
4. ✅ Repoint the dead Dataview query (A2)
5. ✅ Move `Home_old.md` → `Archive/`, `Mom`/`Nana` → `People/` (C3, C4)

> **Before doing A1, consider Bases instead.** `.obsidian/core-plugins.json` has
> `bases: true` — Obsidian Bases is built in and does table views over frontmatter with
> no community plugin and no third-party abandonment risk. Most of your queries (list by
> folder, sort by `file.mtime`, filter by tag) should translate. The one I'm not
> confident about is Home's orphan query, `length(file.inlinks) = 0` — link-graph
> functions may have no Bases equivalent. Worth verifying that single query before
> choosing, since it decides whether you rewrite ~12 blocks or install Dataview.

Decision required before proceeding:

6. **Resolve the Inbox spec contradiction (B1)** — blocks all Inbox work
7. **Confirm what happened to the 61 sensitive conversations (B2)**
8. Decide: strip `related_*` from 22 files and correct the changelog, or amend rule 4 to
   permit them (C1)

Editing passes, do last:

9. Lead sentences on 26 notes (C2)
10. Aliases (D5), template consolidation (C5), README de-duplication (D4)

---

## What I did not check

- **Transcript content.** I surveyed all 584 by frontmatter and filename, but read none in
  full. The "content review" leg — stale facts, contradictions between transcripts, things
  worth promoting into `Notes/` — is a separate job of real size (5.5 MB), and it's gated on
  B1: if Spec 1 wins, most of it gets deleted rather than reviewed.
- **Factual accuracy of `Notes/` articles.** I checked them against the vault's own rules,
  not against reality. Whether your documented network stack matches your actual network,
  I can't tell from the files.
- **Whether the 6 missing articles (D2) are intentional stubs or oversights.**

Counts here are from a scripted pass and should be reliable; the judgment calls about
severity are mine and worth disagreeing with.
