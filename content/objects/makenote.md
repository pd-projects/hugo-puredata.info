---
title: makenote
description: schedule delayed 'note off' message for a note-on
categories:
- object
pdcategory: I/O via MIDI, OSC, and FUDI
last_update: '0.33'
see_also:
- stripnote
arguments:
- type: 1st - float
  description: initial velocity value (default 0).
- type: 2nd - float
  description: initial duration value (default 0).
inlets:
  1st:
    float: MIDI pitch.
  2nd:
    float: MIDI velocity.
  3rd:
    float: MIDI note duratin in ms.
outlets:
  1st:
    float: MIDI pitch.
  2nd:
    float: MIDI velocity.
draft: false
---
Makenote makes MIDI-style note-on/note-off pairs,  which you can use for MIDI output or to drive note-like processes within Pd. It can deal with any numbers (negative,  floats,  whatever) even though MIDI values need to be integers from 0 to 127!

numbers at left are "pitches" which may be integers or not.
