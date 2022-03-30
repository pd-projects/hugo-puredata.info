---
title: ctlout
description: MIDI output
categories:
- object
pdcategory: I/O via MIDI, OSC, and FUDI
last_update: 0.48-2
see_also:
- notein
- noteout
arguments:
- type: float
  description: MIDI controller number
- type: float
  description: MIDI channel/port
inlets:
  1st:
    float: MIDI controller value.
  2nd:
    float: MIDI controller number
  3rd:
    float: MIDI channel/port
bref: MIDI output
draft: false
---

