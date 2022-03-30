---
title: polytouchin
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
  description: channel/port
outlets:
  1st:
    float: MIDI aftertouch value.
  2nd:
    float: MIDI note number
  3rd:
    float: channel/port
  'n: (number depends on number of arguments)': {}
bref: MIDI input
draft: false
---

