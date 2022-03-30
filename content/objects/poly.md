---
title: poly
description: MIDI-style polyphonic voice allocator.
categories:
- object
pdcategory: I/O via MIDI, OSC, and FUDI
last_update: '0.25'
see_also:
- makenote
- route
arguments:
- type: 1) float
  description: number of voices (default 1).
- type: 2) float
  description: non-zero sets to voice stealing.
inlets:
  1st:
    clear: clear memory.
    float: MIDI pitch value.
    stop: flush hanging note on messages.
  2nd:
    float: set velocity value.
outlets:
  1st:
    float: the voice number.
  2nd:
    float: note pitch.
  3rd:
    float: note velocitty.
draft: false
---
The poly object takes a stream of pitch/velocity pairs and outputs triples containing voice number, pitch and velocity. You can pack the output and use the route object to route messages among a bank of voices depending on the first outlet. Another option is to connect it [clone] so you can route to different copies. Poly can be configured to do voice stealing or not (the default.)
