---
title: "[noteout], [ctlout], [bendout], [pgmout], [touchout], [polytouchout], [midiout]"
description: "MIDI output"
bref: "MIDI output"
draft: false
categories: ["object"]
pd-category: "I/O via MIDI, OSC, and FUDI"
---

### [noteout], [ctlout], [bendout], [pgmout], [touchout], [polytouchout], [midiout]


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

INLETS:

- 1st: 
 
  - float - MIDI note number.
  
- 2nd: 

  - float - MIDI velocity
  
- 3rd: 

  - float - MIDI channel/port

OUTLETS:

- NONE.
  
ARGUMENTS:

- float - MIDI channel/port

----------------
  
### [ctlout]

INLETS:

- 1st: 
 
  - float - MIDI controller value.
  
- 2nd: 

  - float - MIDI controller number
  
- 3rd: 

  - float - MIDI channel/port

OUTLETS:
  
- NONE.
  
ARGUMENTS:

- 1st - float - MIDI controller number

- 2nd - float - MIDI channel/port
  
----------------------

### [bendout]

INLETS:

- 1st: 
 
  - float - MIDI bend value.
  
- 2nd: 

  - float - MIDI channel/port

OUTLETS:
  
- NONE.
  
ARGUMENTS:

- float - MIDI channel/port

**Known bug:** [bendin] and [bendout] are inconsistent ([bendin] outputs values from 0 to 16383 and [bendout] takes values from -8192 to 8191) - this won't change.

-----------------

### [pgmout]

INLETS:

- 1st: 
 
  - float - MIDI program value.
  
- 2nd: 

  - float - MIDI channel/port

OUTLETS:
  
- NONE.
  
ARGUMENTS:

- float - MIDI channel/port

**Known bug:** Program change values in [pgmin] and [pgmout] are indexed from 1, which means that the possible values are from 1 to 128 (not 0 to 127)!
  
----------------------

### [touchout]

INLETS:

- 1st: 
 
  - float - MIDI aftertouch value.
  
- 2nd: 

  - float - MIDI channel/port

OUTLETS:
  
- NONE.
  
ARGUMENTS:

- float - MIDI channel/port
  
--------------------

### [polytouchout]

INLETS:

- 1st: 
 
  - float - MIDI aftertouch value.
  
- 2nd: 

  - float - MIDI note number
  
- 3rd: 

  - float - channel/port

OUTLETS:
  
- NONE.
  
ARGUMENTS:

- float - channel/port

-------------------------

### [midiout]

INLETS:

- 1st: 
 
  - float - raw MIDI byte by byte
  
- 2nd: 

  - float - MIDI channel/port

OUTLETS:
  
- NONE.
  
ARGUMENTS:

- NONE.


--------------------

> see also [[notein]](../midi-in) (etc) - MIDI in objects.

> updated for Pd version 0.48-2