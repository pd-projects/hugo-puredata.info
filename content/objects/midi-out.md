---
title: noteout], [ctlout], [bendout], [pgmout], [touchout], [polytouchout], [midiout
description: MIDI output
bref: MIDI output
categories:
- object
last_update: 0.48-2
see_also:
- notein
arguments:
  1st - float: MIDI controller number
  2nd - float: MIDI channel/port
  float: MIDI channel/port
inlets:
  1st:
    float: MIDI note number.
  2nd:
    float: MIDI velocity
  3rd:
    float: MIDI channel/port
draft: false
pdcategory: I/O via MIDI, OSC, and FUDI

---
MIDI OUTPUTS: Outputs are set to channel 1 / port 1 by default, but they also take a channel/port argument (where channels from 17 represent port 2, from 33 port 3 and so on). The [ctlout] object takes control and channel/port arguments. Inlets are not suppressed by arguments and change the parameters.

[[noteout]](#noteout)\
[[ctlout]](#ctlout)\
[[bendout]](#bendout)\
[[pgmout]](#pgmout)\
[[touchout]](#touchout)\
[[polytouchout]](#polytouchout)\
[[midiout]](#midiout)


--------------------

### [noteout]
