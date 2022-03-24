---
title: "[notein], [ctlin], [bendin], [pgmin], [touchin], [polytouchin], [midiin], [midirealtimein], [sysexin]"
description: "MIDI input"
bref: "MIDI input"
draft: false
categories: ["object"]
pdcategory: "I/O via MIDI, OSC, and FUDI"
---

### [notein], [ctlin], [bendin], [pgmin], [touchin], [polytouchin], [midiin], [midirealtimein], [sysexin]

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

INLETS:

- NONE.

OUTLETS:

- n: (number depends on number of arguments)

- 1st: 
 
  - float - MIDI note number.
  
- 2nd: 

  - float - MIDI velocity
  
- 3rd: 

  - float - MIDI channel/port
  
ARGUMENTS:

- float - MIDI channel/port
  
--------------------

### [ctlin]

INLETS:

- NONE.

OUTLETS:

- n: (number depends on number of arguments)

- 1st: 
 
  - float - MIDI controller value.
  
- 2nd: 

  - float - MIDI controller number
  
- 3rd: 

  - float - MIDI channel/port
  
ARGUMENTS:

- 1st - float - MIDI controller number

- 2nd - float - MIDI channel/port
  
----------------------

### [bendin]

INLETS:

- NONE.

OUTLETS:

- n: (number depends on number of arguments)

- 1st: 
 
  - float - MIDI bend value.
  
- 2nd: 

  - float - MIDI channel/port
  
ARGUMENTS:

- float - MIDI channel/port

**Known bug:** [bendin] and [bendout] are inconsistent ([bendin] outputs values from 0 to 16383 and [bendout] takes values from -8192 to 8191) - this won't change.
  
----------------------

### [pgmin]

INLETS:

- NONE.

OUTLETS:

- n: (number depends on number of arguments)

- 1st: 
 
  - float - MIDI program value.
  
- 2nd: 

  - float - MIDI channel/port
  
ARGUMENTS:

- float - MIDI channel/port

**Known bug:** Program change values in [pgmin] and [pgmout] are indexed from 1, which means that the possible values are from 1 to 128 (not 0 to 127)!
  
----------------------

### [touchin]

INLETS:

- NONE.

OUTLETS:

- n: (number depends on number of arguments)

- 1st: 
 
  - float - MIDI aftertouch value.
  
- 2nd: 

  - float - MIDI channel/port
  
ARGUMENTS:

- float - MIDI channel/port
  
--------------------

### [polytouchin]

INLETS:

- NONE.

OUTLETS:

- n: (number depends on number of arguments)

- 1st: 
 
  - float - MIDI aftertouch value.
  
- 2nd: 

  - float - MIDI note number
  
- 3rd: 

  - float - channel/port
  
ARGUMENTS:

- float - channel/port

  
----------------------

These three below are always omni, don't take arguments and output the port number on the right outlet:

### [midiin]

INLETS:

- NONE.

OUTLETS:

- 1st: 
 
  - float - raw MIDI byte by byte (except real-time messages)
  
- 2nd: 

  - float - MIDI channel/port
  
ARGUMENTS:

- NONE.
  
---------------------------

### [midirealtimein]

INLETS:

- NONE.

OUTLETS:

- 1st: 
 
  - float - MIDI real-time messages
  
- 2nd: 

  - float - MIDI channel/port
  
ARGUMENTS:

- NONE.
  
----------------------------

### [sysexin]

INLETS:

- NONE.

OUTLETS:

- 1st: 
 
  - float - MIDI system exclusive messages only, byte by byte
  
- 2nd: 

  - float - MIDI channel/port
  
ARGUMENTS:

- NONE.

--------------------

> see also [[noteout]](../midi-out) (etc) - MIDI out objects.

> updated for Pd version 0.48-2