---
title: Fitness
type: moc
tags: [fitness, hermes]
---

Strength training, conditioning, and bodyweight — the program I'm running and the system that tracks it.

## Current program

- **Program:** Wendler 5/3/1, four lifting days a week, coached and logged by [[Hermes Agent]]
- **Started:** 2026-06-06 (calibration week); Cycle 1 began 2026-06-15
- **Goal:** Rebuild strength after a layoff since October, drop from 187.2 lb to 178 lb at 0.75–1.0 lb/week, and get back to pain-free running

Full program rules, assistance preferences, and coaching behaviour live in the Hermes skill
`wendler-531-coach`. See [[Workout Tracker]] for where the data is stored and how I interact with it.

## Training maxes

Current as of Cycle 2, August 2026. TM is 90% of estimated 1RM; it rises every cycle
(+5 lb upper, +10 lb lower).

- **Squat** — 205 lb
- **Bench Press** — 165 lb
- **Deadlift** — 245 lb
- **Overhead Press** — 115 lb

Starting TMs from June 2026 calibration were 195 / 160 / 235 / 110. Old pre-layoff 1RMs were
roughly 300 squat, 225 bench, 300 deadlift, 145 OHP — the program is deliberately rebuilding
under those, not chasing them.

## Weekly schedule

- **Mon** — Squat
- **Tue** — Kickboxing
- **Wed** — BJJ
- **Thu** — Bench Press
- **Fri** — Deadlift
- **Sat** — Overhead Press
- **Sun** — Rest or easy run

Abs at the end of every lifting session. Easy cardio two-a-days get added gradually as
conditioning allows, never at the cost of the main lifts or recovery.

## Open threads

- **Knee, running:** symptoms historically appear around 2.5–3 mi at sub-11:00/mi pace and
  resolve when I slow down — an intensity problem, not a distance ceiling. Easy pace target is
  11:15–12:00/mi. Need three consecutive symptom-free easy runs before reintroducing faster
  work; build distance to ~6 mi first, pace after.
- **Deadlift grip:** chronic left-hand issue, improving — hit 225x5 double-overhand in July 2026.
  Grip is not allowed to cap the deadlift TM.
- **Bodyweight:** judged on the 7-day rolling average only, never a single reading.

## Related

- [[Workout Tracker]] — the system: what's logged, where it lives, how I use it
- [[Hermes Agent]] — the assistant that coaches and records all of this

## Recent sessions

```dataview
TABLE file.mtime AS "Date"
FROM "Logs"
WHERE domain = "Fitness"
SORT file.mtime DESC
LIMIT 15
```
