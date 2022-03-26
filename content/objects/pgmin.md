---
title: pgmin
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
    float: MIDI program value.
  2nd:
    float: MIDI channel/port
  'n: (number depends on number of arguments)': {}
draft: false
pdcategory: I/O via MIDI, OSC, and FUDI

---
**Known bug:** Program change values in [pgmin] and [pgmout] are indexed from 1, which means that the possible values are from 1 to 128 (not 0 to 127)!
