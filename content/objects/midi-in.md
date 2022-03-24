---
title: notein], [ctlin], [bendin], [pgmin], [touchin], [polytouchin], [midiin], [midirealtimein],
  [sysexin
description: MIDI input
bref: MIDI input
categories:
- object
last_update: 0.48-2
see_also:
- noteout
arguments:
  1st - float: MIDI controller number
  2nd - float: MIDI channel/port
  float: MIDI channel/port
outlets:
  1st:
    float: MIDI note number.
  2nd:
    float: MIDI velocity
  3rd:
    float: MIDI channel/port
  'n: (number depends on number of arguments)': {}
draft: false
pdcategory: I/O via MIDI, OSC, and FUDI

---
MIDI INPUTS: Inputs are omni by default, an optional argument sets the channel/port and removes the rightmost outlet (which outputs this information). For [ctlin], a first optional argument sets controller number and suppresses its corresponding outlet, and a second argument sets the channel and also suppresses its corresponding outlet.

Port number is encoded as the channel number. Channels 1 to 16 are for port 1, channels 17 to 32 is the same as channels 1 to 16 for port 2, channels 33 to 48 represents channels 1 to 16 in port 3, and so on...

[[notein]](#notein)\
[[ctlin]](#ctlin)\
[[bendin]](#bendin)\
[[pgmin]](#pgmin)\
[[touchin]](#touchin)\
[[polytouchin]](#polytouchin)\
[[midiin]](#midiin)\
[[midirealtimein]](#midirealtimein)\
[[sysexin]](#sysexin)

-----------------------------

### [notein]
