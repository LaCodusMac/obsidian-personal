---
title: "Workout Tracker"
aliases: [Workouts, 5/3/1 Tracker, Wendler Tracker]
type: project
status: active
priority: medium
started: 2026-01-01
tags: [project, hermes, fitness, telegram]
---

A workout tracker that [[Hermes Agent]] **built for me** — I created it by instructing Hermes through the Telegram chat, which is a good example of Hermes turning instructions into a real, working project rather than just answering. I log and query workouts through that same chat.

See [[Fitness]] for the program itself, current training maxes, and open training threads.

## What gets logged

Everything goes into one Excel workbook with five sheets:

- **Log** — every lifting set: date, cycle, week, lift, set number, prescribed weight and reps,
  actual reps completed on the AMRAP set, estimated 1RM, and a notes field. Missed sessions are
  logged too, as rows with null weights and a note explaining why — the gaps are data.
- **Training Maxes** — current TM per lift plus the history of every TM change by cycle.
- **Bodyweight** — date, weight, notes.
- **Conditioning** — runs, BJJ, kickboxing: date, activity, duration, distance, notes. Run
  entries capture pace, elevation, and knee symptoms.
- **Program** — program rules and reminders.

Estimated 1RM is computed on every top set as `weight × reps × 0.0333 + weight`. Hermes flags
week-over-week jumps above ~10% rather than letting the TM chase a fluke.

## Where it lives

All on the machine Hermes runs on, under `~/.hermes/workout-531/`:

- `workout_tracker.xlsx` — the workbook described above
- `state.json` — the live program state: current cycle and week, training maxes, calibration
  results per lift, weekly schedule, assistance preferences, running notes, bodyweight targets,
  and a running list of recent sessions with full detail. This is what Hermes reads to answer
  "what's today's workout."
- `weight.py` — bodyweight CLI, writes to the Bodyweight sheet
- `create_workbook.py` — regenerates the workbook structure

Program *rules* live separately, in the Hermes skill `wendler-531-coach` under
`~/.hermes/skills/fitness/`. Rough split: the skill holds how to coach, `state.json` holds where
I currently am, the workbook holds what actually happened.

Not backed up yet — same gap as [[Backup — Hermes]], and worth folding into that job since both
sit under `~/.hermes/`.

## How I use it

There are no slash commands. It's plain conversation in Telegram — Hermes recognises the intent
and writes to the right sheet.

- **"What's today's workout?"** → reads `state.json`, returns exact sets, reps, and weights for
  the current cycle/week/lift, plus assistance and abs
- **Report a session** → "squat 175x9 today, cut assistance short" gets logged to Log, estimated
  1RM computed, PRs and trends flagged
- **Report a run or BJJ** → logged to Conditioning
- **Report bodyweight** → logged via `weight.py`; judged on the 7-day rolling average only
- **End of a cycle** → Hermes increments the TMs, records the change, and updates `state.json`

Every logged session ends with a short Strava post: a title, a sentence or two describing the
work in words, and a quote. No weights or rep numbers in it — I add those myself if I feel like it.

## Reports

No dashboards or charts. Everything is conversational: rolling bodyweight averages, estimated
1RM trends, and pattern analysis (e.g. correlating knee symptoms against pace across runs) come
back as chat replies on request. A [[Grafana]] view over the workbook is an obvious extension and
hasn't been built.

## Related

- Parent: [[Hermes Agent]]
- Area: [[Fitness]]

## Log

- 2026-07-28: Note created under Hermes.
- 2026-07-28: Clarified it was built *by* Hermes via Telegram instruction — a concrete example of Hermes shipping a project.
- 2026-08-12: Filled in the open questions — storage paths, sheet schema, and the conversational
  interface. Confirmed there are no slash commands and no charts.
