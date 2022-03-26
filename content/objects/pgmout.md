---
title: pgmout
description: MIDI output
bref: MIDI output
categories:
- object
last_update: 0.48-2
see_also:
- notein
- noteout
arguments:
  float: MIDI channel/port
inlets:
  1st:
    float: MIDI program value.
  2nd:
    float: MIDI channel/port
draft: false
pdcategory: I/O via MIDI, OSC, and FUDI

---
**Known bug:** Program change values in [pgmin] and [pgmout] are indexed from 1, which means that the possible values are from 1 to 128 (not 0 to 127)!
