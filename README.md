# Personal Vault — Setup

A personal wiki. Flat article namespace, navigation by links and MOCs, not by folders.

## Structure

```
Home.md        ← dashboard, start here
Notes/         ← THE article namespace. One note per entity. Flat, on purpose.
Logs/          ← dated entries (workouts, print runs, sales, incidents)
MOCs/          ← Maps of Content: hand-curated entry points per area
People/
Inbox/         ← quarantined raw imports. Mine and delete. Not a knowledge base.
Archive/
Templates/
_AI/           ← rules + changelog for AI-assisted maintenance
```

### Why `Notes/` is flat
This is the Wikipedia model: one namespace, no subject folders. It removes the
"which folder does this go in" decision, and — more importantly — it makes
search-before-create natural, which is what actually prevents duplicate notes.

Type lives in frontmatter (`type: device | service | concept | area | howto`),
so Dataview can group by type on demand. If you later decide you want folders,
that field makes the re-sort mechanical.

Rule of thumb: if you'd hesitate about which folder, it belongs in `Notes/`.

## Required setup

**1. Plugins** (Settings → Community Plugins → Browse)
- **Dataview** — required. Home.md is raw query blocks without it.
- **Templater** — optional, one-click new notes from `Templates/`.

**2. Exclude the Inbox from search** (Settings → Files & Links → Excluded files)
Add `Inbox`. This de-prioritizes raw transcripts in search results and quick
switcher. Without this, the Inbox pollutes every lookup you do.

**3. Turn on aliases in the quick switcher** — on by default; just use it.
`aliases:` in frontmatter is the redirect mechanism. It is the single highest-value
habit in this vault. See `Notes/Synology NAS.md` for the pattern.

## The three rules that keep this from rotting

1. **Search before you create.** One canonical note per thing, forever. If a note
   exists, edit it. Add an alias instead of a new note.
2. **Lead sentence first.** Every note opens with one plain line saying what the
   thing is, before any heading or structure.
3. **Drain the Inbox by deleting.** Mine a transcript into the relevant `Notes/`
   article, then delete the transcript. A "reviewed" status flag you have to
   remember to flip is a queue that never drains.
