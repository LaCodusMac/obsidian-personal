# Import Schema & Conventions

This vault is a growing, model-agnostic library of Jacob's AI conversations — a personal
memory store that any AI agent (Claude, ChatGPT, Gemini, a local model, etc.) can read and
query, so no single provider ends up holding the only copy of that context. This document
is the spec: how notes are structured, how they're filed, and how to bring in the next
batch from a different model without breaking consistency.

## Folder structure

```
Staging/                          landing zone for a fresh export, before filing
Library/
  <Category>/*.md                 filed, non-sensitive conversations
  Private/
    <Category>/*.md               filed, sensitive/flagged conversations
    Private Index.md              index of everything in Private/
Conversation Index.md             index of everything in Library/ (excludes Private)
Import Schema.md                  this file
```

Every conversation is one Markdown note. Sensitivity determines whether a note lives under
`Library/<Category>/` or `Library/Private/<Category>/` — the category taxonomy is identical
on both sides, so a note that gets reclassified from sensitive to not (or vice versa) just
moves across that one boundary.

## Frontmatter schema

Every note starts with YAML frontmatter:

```yaml
---
date: 2026-06-08
source: chatgpt
title: "Kalshi Signal Analysis"
category: "Coding & Dev Projects"
tags: [chatgpt-import]
status: pending-review
sensitive: true
flagged_reason: [health]
---
```

| Field | Required | Notes |
|---|---|---|
| `date` | yes | `YYYY-MM-DD`. Conversation date, not import date. |
| `source` | yes | Which model/product the conversation came from: `chatgpt`, `claude`, `gemini`, `grok`, etc. Lowercase, one word per source. Add new values freely as new models are imported — never overload an existing one. |
| `title` | yes | Short human-readable title, quoted if it contains punctuation. |
| `category` | yes | One of the taxonomy values below. Assigned during filing, not at raw export. |
| `tags` | yes | Array. Always includes `<source>-import` (e.g. `chatgpt-import`, `claude-import`). Free-form additional tags are fine (e.g. project threads), but don't rely on them for filing — `category` is the source of truth. |
| `status` | yes | `pending-review` until a human has read the note and confirmed it's filed correctly and safe to keep; then `approved`. |
| `sensitive` | yes | `true`/`false`. Drives Library vs. Private placement. |
| `flagged_reason` | only if `sensitive: true` | Array from the fixed vocabulary: `health`, `financial`, `relationship_family`, `legal_work_conflict`. Add a new reason category here (and document it in this table) rather than inventing one-off values. |

Body: conversation turns as `**You:**` / `**<Model>:**` (e.g. `**ChatGPT:**`, `**Claude:**`)
paragraphs, in order. Keep the original export text as-is (including any inline images,
tool citations, etc.) — don't summarize or edit it during import.

## Category taxonomy

Fifteen categories currently in use. Keep new notes inside these unless a genuinely new
domain shows up in volume (see "Growing the taxonomy" below).

- **Coding & Dev Projects** — software/dev work, including the Kalshi/Hermes trading bot
- **Home Lab, Networking & Smart Home** — self-hosting, Proxmox, Synology, Docker, Pi-hole, UniFi, Home Assistant, smart home devices
- **Finance & Investing** — budgeting, investing, credit, taxes, savings
- **Health & Fitness** — gym, BJJ, medical questions, sleep, nutrition
- **Style & Grooming** — outfits, haircuts, grooming, appearance
- **Career & Work** — resumes, interviews, onboarding, performance reviews
- **Relationships & Social** — dating, breakups, messages to friends/family
- **Design & Creative** — logos, 3D printing, graphics, content creation
- **Home, Apartment & Shopping** — apartment search/move, furniture, electronics purchases
- **Tech Support (General)** — everyday consumer tech troubleshooting (not homelab)
- **Cars & Vehicles**
- **Sports & Entertainment** — UFC/MMA, fantasy sports, movies, music, games
- **Food & Recipes**
- **Learning & Reference** — study guides, general-knowledge questions
- **General & Life Admin** — genuine catch-all: greetings, one-off questions that don't fit elsewhere

## Naming convention

`YYYY-MM-DD-kebab-case-slug.md`, date first so files sort chronologically inside a folder.
Filenames must stay unique across the *entire* vault, not just within a category — Obsidian
wikilinks (`[[note-name]]`) resolve by filename, and a duplicate elsewhere would create an
ambiguous link. If two conversations would produce the same slug, disambiguate with a
suffix (`-2`, `-3`, ...).

## Sensitive content handling

On import, notes are scanned with a keyword heuristic (not a guarantee) and flagged
`sensitive: true` with one or more `flagged_reason` values when they touch health,
financial, relationship/family, or legal/work-conflict topics. Flagged notes are filed
into `Library/Private/<Category>/` instead of `Library/<Category>/`, and are listed in
`Library/Private/Private Index.md` rather than the main `Conversation Index.md`.

This is a first pass, not a final judgment — skim `Private Index.md` yourself, and skim the
rest too if you want to be thorough. Once reviewed, either flip `sensitive: false` and move
the note over to `Library/<Category>/`, or leave it, redact it, or delete it.

## Importing a new batch (e.g. from Claude, Gemini, Grok)

1. Export the raw conversations from the source product.
2. Convert each conversation to one Markdown note with the frontmatter above —
   `source` set to the new model name, `sensitive`/`flagged_reason` run through the same
   keyword heuristic (health/financial/relationship_family/legal_work_conflict), `status:
   pending-review`, `category` left unset for now.
3. Drop the notes into `Staging/`.
4. Classify each note into one of the taxonomy categories above, using title + a skim of
   the body — same approach as the existing library, so results stay consistent.
5. Move `sensitive: true` notes to `Library/Private/<Category>/`, everything else to
   `Library/<Category>/`; delete the now-empty files from `Staging/`.
6. Add each new note as a checklist entry to `Conversation Index.md` or
   `Library/Private/Private Index.md`, under the right category heading.

## Growing the taxonomy

If a new source starts producing a real cluster of conversations that don't fit any
existing category (not just one or two stray notes — those belong in General & Life
Admin), add a new category: create the folder under both `Library/` and
`Library/Private/`, add a heading for it in both index files, and document it in the
taxonomy list above. Avoid categories with fewer than ~10 notes; fold small clusters into
the closest existing category instead.

## Why this shape

Consistent `source`, `category`, `date`, `sensitive`, and `tags` fields mean any AI agent
pointed at this vault — Claude reading it via file tools, an Obsidian Dataview query, a
future local search index — can filter and retrieve relevant past context (e.g. "everything
tagged Coding & Dev Projects from any source, sorted by date") without needing to re-read
the whole library or depend on any single provider's memory feature.
