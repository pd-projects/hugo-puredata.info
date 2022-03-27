---
title: poly
description: MIDI-style polyphonic voice allocator.
categories:
- object
last_update: '0.25'
see_also:
- makenote
- route
arguments:
  1) float: number of voices (default 1).
  2) float: non-zero sets to voice stealing.
inlets:
  1st:
    float: MIDI pitch value.
    clear: clear memory.
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
pdcategory: I/O via MIDI, OSC, and FUDI

---
The poly object takes a stream of pitch/velocity pairs and outputs triples containing voice number, pitch and velocity. You can pack the output and use the route object to route messages among a bank of voices depending on the first outlet. Another option is to connect it [clone] so you can route to different copies. Poly can be configured to do voice stealing or not (the default.)
