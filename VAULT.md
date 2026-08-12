---
title: VAULT
type: meta
---

# VAULT.md — the canonical spec

**This file is the single source of truth for how this vault is structured, formatted, and
grown.** If any other document contradicts it, this one wins and the other one is a bug.

That rule exists for a reason. Until 2026-08-03 the vault had two documents describing the
same folder in opposite terms — one called it disposable quarantine, the other called it a
permanent memory store. Both were followed inconsistently for months. Duplicated
descriptions drift; one canonical file is the fix.

Read this first. `README.md` and `_AI/AI Maintenance Guide.md` are short pointers to it.

---

## 1. What this vault is

A personal wiki plus a permanent AI-conversation corpus. **Two layers, different jobs:**

| | `Notes/` + `People/` + `MOCs/` + `Logs/` | `Library/` |
|---|---|---|
| Contains | Curated articles, one per thing | Verbatim AI conversation transcripts |
| Authority | **Authoritative.** States what is true now. | **Not authoritative.** Records what was said. |
| Written by | You, or an agent under these rules | Exported verbatim, never edited |
| Grows by | Deliberate writing | Bulk import |
| Edited? | Yes, continuously | **Never** |
| Deleted? | No — archived instead | **Never** |
| Cite it? | Yes | No |

The distinction is the whole design. **Cite articles, never transcripts.** A transcript
records what a model said on a Tuesday in 2024; it may be wrong, superseded, or contradicted
by another transcript three files over. If something in `Library/` is true, write it into an
article, and cite the article.

The corpus is model-agnostic on purpose: no single provider should end up holding the only
copy of your context.

---

## 2. Structure

```
VAULT.md        ← this file. The spec.
CLAUDE.md       ← agent entry point; points here
README.md       ← human setup; points here
Home.md         ← dashboard

Notes/          ← THE article namespace. One note per thing. Flat, on purpose.
People/         ← one note per person
MOCs/           ← Maps of Content: hand-curated entry points per area
Logs/           ← dated entries (workouts, print runs, incidents)
Archive/        ← superseded notes, never deleted
Library/        ← permanent AI conversation corpus. Flat. Append-only.
Templates/      ← note skeletons
_AI/            ← maintenance guide, changelog, tooling
```

### Why everything is flat

`Notes/` and `Library/` are both flat namespaces with no subject subfolders. This is the
Wikipedia model. It removes the "which folder does this go in" decision, and — more
importantly — it makes search-before-create natural, which is what actually prevents
duplicate articles.

Classification lives in frontmatter (`type:` for articles, `category:` for transcripts), so
queries can group on demand and a future re-sort is mechanical.

**Rule of thumb: if you'd hesitate about which folder, it belongs in `Notes/`.**

### Where a new note goes

| It is… | Goes to | Type |
|---|---|---|
| A device, service, concept, or reference article | `Notes/` | see §3 |
| A procedure for fixing something | `Notes/` | `runbook` |
| A person | `People/` | `person` |
| A dated, repeating entry | `Logs/` | `log` |
| An area entry point | `MOCs/` | `moc` |
| An imported AI conversation | `Library/` | — (see §5) |
| Superseded by something else | `Archive/` | unchanged |

---

## 3. Frontmatter

Frontmatter carries **only what a query actually needs.** Everything else is body text.

### Universal

```yaml
---
title: "Synology NAS"        # required. Quote if it contains punctuation.
aliases: [NAS, DS920+]       # optional but high value — see §4
type: device                 # required. Vocabulary below.
tags: [homelab, storage]     # optional
---
```

### `type:` vocabulary

Fixed list. Don't invent values; if none fits, the note probably belongs to an existing one.

| Type | Means | Lives in |
|---|---|---|
| `hub` | The dashboard. Exactly one. | `Home.md` |
| `moc` | Map of Content, an area entry point | `MOCs/` |
| `area` | An ongoing responsibility with no end date | `Notes/` |
| `project` | Something with a beginning and an end | `Notes/` |
| `resource` | A reference article or a scoped task | `Notes/` |
| `runbook` | A procedure: symptom → fix | `Notes/` |
| `device` | Physical hardware | `Notes/` |
| `service` | Software that runs somewhere | `Notes/` |
| `concept` | An idea or pattern, not a thing you own | `Notes/` |
| `person` | A person | `People/` |
| `log` | A dated entry | `Logs/` |
| `meta` | A document about the vault itself | `_AI/`, `Library/` |

### Conditional fields

| Field | When | Notes |
|---|---|---|
| `status` | `project`, `resource` tasks | `not-started` / `active` / `blocked` / `done` |
| `priority` | tasks | `low` / `medium` / `high` |
| `host` | anything that runs on a machine | which machine |
| `domain` | `log` only | which MOC the log belongs to |
| `date` | `log` only | `YYYY-MM-DD` |
| `role` | `person` only | |

### Two fields that are banned

**`related_*` — banned.** No `related_projects`, `related_people`, `related_areas`,
`related_resources`. Use inline `[[wikilinks]]` in the body. The same relationship recorded
twice by hand drifts, and a drifting Dataview table is worse than no table because it fails
silently. Obsidian's backlinks pane gives you the reverse direction for free.

**`updated:` — banned.** Dataview reads `file.mtime`. A hand-written date is one more thing
to forget, and when it's wrong the staleness report lies.

---

## 4. Writing conventions

### 4.1 One article per thing, forever
Search before you create. If an article exists, edit it. If the name differs, **add an alias
to the existing note** — do not create a second article. Duplicate articles are the primary
failure mode of this vault.

### 4.2 Lead sentence first
Every note opens with **one plain sentence saying what the thing is, before any heading.**

```markdown
---
title: "Prusa Mini"
type: device
---

A Prusa Mini+ 3D printer on the shelf in the office, used mostly for functional PLA parts.

## Current state
...
```

Not:

```markdown
# Prusa Mini          ← don't open with the heading

## Current state
```

If you can't write that sentence, you don't understand the note well enough to edit it.

The H1 is redundant with `title:` and the filename — Obsidian already shows both.

### 4.3 Current state vs. log
Article bodies state what is **true now**. Superseded facts move to a `## Log` section with a
date, or to `Logs/` if the volume is high. **Never leave two contradictory claims in a body.**

### 4.4 Links
Inline `[[wikilinks]]`, in prose, where the relationship is actually being described. Links
resolve by **filename or alias** — `title:` in frontmatter does nothing for resolution.

Filenames use **spaces, not underscores**, so `[[Synology NAS]]` resolves. A note named
`Synology_NAS.md` will silently fail to match every link written the natural way.

Linking to an article that doesn't exist yet is fine and useful — it's a writing queue. Just
know that's what you're doing.

### 4.5 Aliases
`aliases:` is the redirect mechanism and the single highest-value habit here. When you type
`[[NAS`, autocomplete should land on the existing article rather than tempt you into a second
one. See `Notes/Synology NAS.md` for the pattern.

### 4.6 Voice
Short, plain, no filler. Bullets over paragraphs. No hedging in an article body — if
something is uncertain, say so explicitly and date it.

---

## 5. Importing into `Library/`

Full format spec: `Library/Import Schema.md`. Philosophy: `Library/About the Library.md`.
Summary of the workflow:

1. Export conversations from the source product.
2. Convert each to one markdown note, `YYYY-MM-DD-kebab-case-slug.md`, filename unique
   across the **whole vault** (wikilinks resolve by filename).
3. Frontmatter: `date`, `source` (`chatgpt` / `claude` / `gemini` / …), `title`, `tags`
   (always includes `<source>-import`), `sensitive`. Leave `category` unset.
4. Drop them straight into `Library/`. Unset `category` is what marks a note unfiled — no
   staging folder to remember to empty.
5. Assign `category` from the fixed taxonomy in `Import Schema.md`.
6. **Apply the `.private.md` suffix to anything `sensitive: true`** (see §6).
7. Run `python3 _AI/regenerate_index.py`. It rebuilds both indexes and fails loudly on
   mistakes. Never hand-edit the indexes.

### Rules for transcripts

- **Never edit a body.** Not to summarize, reword, fix typos, or tidy. The value is being a
  verbatim record; an edited transcript is worse than none because it looks authoritative
  while being neither original nor curated.
- **Never delete one.** There is no review queue and no backlog. The corpus is valuable for
  coverage, not tidiness.
- **Promotion ≠ deletion.** When a conversation contains something worth stating as settled
  fact, write it into a `Notes/` article in your own words. The transcript stays. The article
  says what's true; the transcript records how you got there.

---

## 6. Sensitive material

Conversations touching health, finances, family/relationships, or legal-work conflict:

- named `YYYY-MM-DD-slug.**private**.md`
- carry `sensitive: true` and a `flagged_reason`
- live flat in `Library/` like everything else — same search, same agent access
- are **excluded from git** by one wildcard in `.gitignore`
- are indexed in `Private Index.private.md`, itself gitignored

**The suffix is load-bearing.** It is what `.gitignore` matches. A sensitive note without it
gets committed, and it looks completely normal — which is why `regenerate_index.py` checks
for exactly this and asks git directly whether each file is really ignored.

Why git specifically: it's the one place where deleting something later doesn't remove it,
and repo visibility can change retroactively. The filename set is itself sensitive, which is
why `.gitignore` uses a wildcard rather than a list — that file is committed too.

**What this does not do:** encrypt anything. These are plaintext to anyone with vault or
Obsidian Sync access, by design, because agents must be able to read them. The boundary is
"not in a remote git repo," not "secret." Some of this content concerns other people —
family health, coworkers in work disputes — which is worth remembering before pointing a new
tool or service at this vault.

---

## 7. Maintenance

### 7.1 Never silently delete
Move to `Archive/` with a dated line saying why. No exceptions — `Library/` in particular is
append-only.

### 7.2 Log every session
Append a dated entry to `_AI/Changelog.md`: what changed and why. This is how a human audits
without re-reading every file, so **it has to be accurate**. An entry claiming a cleanup that
didn't happen is worse than no entry — it was wrong once already, on 2026-07-31.

### 7.3 Ask before restructuring
Renaming folders, merging articles, or changing this schema affects everything. Propose, get
a yes, then do it.

### 7.4 Use `Library/` before researching from scratch
584 conversations, 2023–2026, are already there. Prior context beats re-derivation. Treat
what you find as history, not fact: confirm against the article, and if the two disagree, the
article wins and the disagreement is worth flagging.

### 7.5 Health checks
```bash
python3 _AI/regenerate_index.py     # index + sensitive-file integrity
```
`Home.md` surfaces stale notes, orphans, and unfiled transcripts — once a query engine is
installed (see `README.md`).

---

## 8. Known open items

- **No query engine installed.** `Home.md` is raw query blocks until Dataview is added or the
  built-in Bases plugin is wired up. Everything else works regardless. This is the only thing
  blocking the dashboard.
- **Six intentional stubs.** `[[Proxmox]]`, `[[Plex]]`, `[[Pi-hole]]`, `[[Grafana]]`,
  `[[Home Assistant]]`, `[[Tailscale]]` are linked from `MOCs/` and `Notes/Synology NAS.md`
  but not yet written. **This is deliberate** — they're a writing queue, confirmed
  2026-08-03. A link checker will flag them; that's expected, not a defect.
- **`Logs/` has no entries yet.** Structure and conventions are in place
  (`Logs/About Logs.md`); nothing has started being logged.
- **Sensitivity flags are over-broad.** All 61 imported `sensitive: true` notes are treated
  as private, but the keyword heuristic clearly over-fired — a cheese review and a Korean War
  overview are in there. Reclassifying is safe and reversible; leaving them private costs
  nothing but index noise. See §6.
- **Backups are not running.** `Notes/Backups.md` and its seven service notes describe the
  plan; none of it is implemented. `Backup — Hermes` is the one flagged irreplaceable.
