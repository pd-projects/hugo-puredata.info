---
title: "[ctlin]"
description: "MIDI input"
bref: "MIDI input"
draft: false
categories: ["object"]
pd-category: "I/O via MIDI, OSC, and FUDI"
---

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
 
> see also [[notein]](../notein) (etc) - MIDI in objects.

> see also [[noteout]](../noteout) (etc) - MIDI out objects.

> updated for Pd version 0.48-2