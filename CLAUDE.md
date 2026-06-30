# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Negative Space** — a minimalist, mobile-first HTML5 canvas survival game. You are a tiny dot. Soft iridescent ink blobs bloom and spread across a warm off-white field, consuming the space. You survive only in the white that remains. The whole game is a single self-contained `index.html` (inline CSS + JS, no build step, no dependencies).

## Concept

The danger is not the obstacles — it's the *absence of space*. You perceive only yourself and the shrinking emptiness around you. Survive long enough that the void becomes full and you win.

## Running the Game

Open `index.html` directly in a browser, or serve it statically:

```bash
python3 -m http.server 8080
# then open http://localhost:8080
```

## Architecture (all in `index.html`)

- **Palettes** — curated iridescent colour sets (`COOL` / `HOT`), each baked into a soft lobe sprite.
- **Liquid blobs (metaballs)** — each blob is several lobe sprites (`makeLobes`) that drift & swell on independent sine waves, so the silhouette morphs like ink. Bigger blobs are more liquid and pulse harder (size factor `sf`).
- **Film grain** — a pre-rendered noise tile overlaid each frame for a printed, risograph texture.
- **Spawning** — irregular cadence with bursts (`spawnShape`), near-player ambushes (`spawnAmbush`) and an anti-camp flush (`spawnFlush`). `spawnNear` guarantees blobs never appear under the cursor, even in corners.
- **Scoring** — score is the **% of the void survived**, measured precisely by sampling a grid (`measureOccupancy`) against each blob's lethal footprint. A progress bar tracks it; reaching `WIN_FILL` coverage = **win** (success screen).
- **State machine** — `state`: `"intro"` → `"playing"` → `"over"` | `"won"`.
- **Audio** — Web Audio synth. Everything is built from one soft sine `bloomNote`; start, spawn, and end cues share that voice as a family.

## Key Constants

| Constant | Purpose |
|---|---|
| `WIN_FILL` | Lethal coverage fraction that counts as a full void → win (0.62) |
| `PLAYER_R` | Player dot radius |
| `LOBE` / `LOBE_PAD` | Lobe sprite resolution & padding |
| `difficulty()` | Time-driven curve: spawn rate, growth speed, blob size, ambush frequency |

## Notes

- Pure vanilla — no frameworks, no assets, no fonts beyond the system sans stack.
- DPR-aware rendering keeps gradients and type crisp on retina displays.
