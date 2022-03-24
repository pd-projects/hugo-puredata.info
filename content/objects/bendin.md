---
title: "[bendin]"
description: ""
bref: ""
draft: false
categories: ["object", "I/O via MIDI, OSC, and FUDI"]
---

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

> see also [[notein]](../notein) (etc) - MIDI in objects.

> see also [[noteout]](../noteout) (etc) - MIDI out objects.

> updated for Pd version 0.48-2
 
