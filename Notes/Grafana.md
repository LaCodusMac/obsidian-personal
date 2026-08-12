---
title: "Grafana"
aliases: [Grafana dashboards, kalshi-grafana, metrics dashboards]
type: service
tags: [homelab, monitoring, selfhosted, observability]
---

Metrics dashboards. **There are two entirely separate Grafana instances in the lab**, on different machines, serving different data — conflating them is the standing failure mode with this note, so they're kept apart below.

## Instance 1 — lab monitoring, on [[NUC10]]

- Docker container `grafana` (image `grafana/grafana`), port **3000**
- Fed by **Prometheus** (9090) and **node-exporter** (9100) on the same host
- Config/data under `prometheus/` on NUC10 (`prometheus.yml`, `alerts.yml`, `compose.yaml`, `data/`, `grafana/`)
- Purpose: host and container metrics for the lab itself
- ⚠️ Unrecorded: what dashboards actually exist, whether any alerts in `alerts.yml` are wired to a notification channel, and whether the admin password is still `admin`

## Instance 2 — KalshiWatch, on the Lenovo P3 Mini

- systemd unit `kalshi-grafana.service`, on `llamaswithhats` alongside [[Hermes Agent]]
- Purpose: visualising the [[KalshiWatch]] prediction-market SQLite data
- Dashboards are stored **as JSON in the KalshiWatch git repo** — version-controlled, so they survive a host loss. See [[Backup — KalshiWatch]]
- ⚠️ **Possible exposure, unverified:** this instance may be bound to `0.0.0.0:3001` with weak hardcoded credentials, which would make it reachable from anywhere on the LAN without meaningful auth. This is recorded here from an outside note, **not** confirmed against the running service — check `kalshi-grafana.service` and the Grafana config on the P3 Mini before treating it as either true or false.

## Depends on

- Instance 1: [[NUC10]], Prometheus, node-exporter
- Instance 2: the P3 Mini, [[KalshiWatch]]'s SQLite database

## Gotchas

- **Two instances, two ports, two hosts.** "Check Grafana" is ambiguous. Say which.
- Dashboards in instance 1 are **not** in git, unlike instance 2's. A NUC10 rebuild loses them unless `prometheus/grafana/` is in the backup set — see [[Backups]].
- Grafana's default credentials are `admin`/`admin` and it only prompts for a change interactively on first login. An instance stood up by compose and never logged into keeps them.

## To verify

- [ ] Confirm or refute the `0.0.0.0:3001` + weak-credentials exposure on the P3 Mini instance
- [ ] Check whether instance 1's admin password was ever changed
- [ ] Confirm `prometheus/grafana/` is included in whatever backup job covers NUC10

## Related

- [[Self-Hosted Software]] · [[NUC10]] · [[KalshiWatch]] · [[Backups]]

## Log

- 2026-08-11 — Note created to resolve the broken `[[Grafana]]` link in `MOCs/Self-Hosted`. Both instances were already documented separately in [[Self-Hosted Software]] and [[NUC10]]; this note consolidates them and preserves the explicit warning against conflating the two. The exposure claim on instance 2 came from context outside the vault and is flagged unverified.
