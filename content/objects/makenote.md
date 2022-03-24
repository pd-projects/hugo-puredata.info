---
title: "[makenote]"
description: "schedule delayed 'note off' message for a note-on"
bref: "schedule delayed 'note off' message for a note-on"
draft: false
categories: ["object"]
pd-category: "I/O via MIDI, OSC, and FUDI"
---

### [makenote]

Schedule delayed 'note off' message for a note-on.

Makenote makes MIDI-style note-on/note-off pairs,  which you can use for MIDI output or to drive note-like processes within Pd. It can deal with any numbers (negative,  floats,  whatever) even though MIDI values need to be integers from 0 to 127!

numbers at left are "pitches" which may be integers or not.


INLET:

- 1st:

  - float - MIDI pitch.

- 2nd:

  - float - MIDI velocity.

- 3rd:

  - float - MIDI note duratin in ms.

OUTLET: 

- 1st:

  - float - MIDI pitch.

- 2nd:

  - float - MIDI velocity.

ARGUMENTS:

- 1st - float - initial velocity value (default 0).

- 2nd - float - initial duration value (default 0).



 
> see also [[stripnote]](../stripnote)

> updated for Pd version 0.33