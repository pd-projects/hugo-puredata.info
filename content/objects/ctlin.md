---
title: ctlin
description: MIDI input
bref: MIDI input
categories:
- object
last_update: 0.48-2
see_also:
- notein
- noteout
arguments:
  1st - float: MIDI controller number
  2nd - float: MIDI channel/port
outlets:
  1st:
    float: MIDI controller value.
  2nd:
    float: MIDI controller number
  3rd:
    float: MIDI channel/port
  'n: (number depends on number of arguments)': {}
draft: false
pdcategory: I/O via MIDI, OSC, and FUDI

---

