---
title: bendin
description: MIDI input
bref: MIDI input
categories:
- object
last_update: 0.48-2
see_also:
- notein
- noteout
arguments:
  float: MIDI channel/port
outlets:
  1st:
    float: MIDI bend value.
  2nd:
    float: MIDI channel/port
  'n: (number depends on number of arguments)': {}
draft: false
pdcategory: I/O via MIDI, OSC, and FUDI

---
**Known bug:** [bendin] and [bendout] are inconsistent ([bendin] outputs values from 0 to 16383 and [bendout] takes values from -8192 to 8191) - this won't change.
