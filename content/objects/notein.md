---
title: notein
description: MIDI input
categories:
- object
pdcategory: I/O via MIDI, OSC, and FUDI
last_update: 0.48-2
see_also:
- ctlin
- noteout
arguments:
- type: float
  description: MIDI channel/port
outlets:
  1st:
    float: MIDI note number.
  2nd:
    float: MIDI velocity
  3rd:
    float: MIDI channel/port
  'n: (number depends on number of arguments)': {}
draft: false
---

