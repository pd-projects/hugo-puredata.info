---
title: touchin
description: MIDI input
categories:
- object
pdcategory: I/O via MIDI, OSC, and FUDI
last_update: 0.48-2
see_also:
- notein
- noteout
arguments:
- type: float
  description: MIDI channel/port
outlets:
  1st:
    float: MIDI aftertouch value.
  2nd:
    float: MIDI channel/port
  'n: (number depends on number of arguments)': {}
bref: MIDI input
draft: false
---

