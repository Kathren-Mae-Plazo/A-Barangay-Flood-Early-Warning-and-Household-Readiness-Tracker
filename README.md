# FloodReady

A barangay flood early-warning and household readiness tracker, written in Python.

## What it does

FloodReady turns two simple signals — the day's rainfall forecast and the
river level reading — into one clear readiness level per household, with the
action that household should take right now.

Readiness levels:
1. Normal — no action needed
2. Prepare — charge devices, check go-bags
3. Evacuate Soon — move valuables up, be ready to leave within 1 hour
4. Evacuate Now — leave immediately via the agreed route

## The problem

Flood warnings in many barangays are scattered across group chats and
Facebook posts, so whether a household hears in time is mostly luck.
FloodReady puts the risk signal and the household's own preparedness
details in one place.

## Planned features

- Register a household (street, members, vulnerable members)
- Compute readiness level from rainfall + river level
- Personalised preparedness checklist
- Log flood events and build a local flood history
- Street risk summary ranked by flood frequency
- Save and load records from text files

## How it will work

Inputs: rainfall forecast, river level, household details, flood event details.
Outputs: readiness level, action guide, checklist, flood history, street summary.

See `proposal.md` for the full logic plan and pseudocode.

## Project status

Initial proposal stage. No working program yet — this repository holds the
proposal and the planned structure only.

## Author

<Kathren Mae I. Plazo> — <8-Rosal>
