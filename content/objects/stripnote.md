---
title: "[stripnote]"
description: "strip 'note off' messages"
bref: "strip 'note off' messages"
draft: false
categories: ["object"]
pd-category: "I/O via MIDI, OSC, and FUDI"
---

### [stripnote]

strip 'note off' messages.

Stripnote ignores note-off (zero-velocity) messages from a stream of MIDI-style note message and passes the others through unchanged. It can deal with any kind of number (negative,  floats,  whatever) even though MIDI values need to be integers from 0 to 127!

The left inlet takes the note number and the right inlet takes velocity values. Alternatively,  you can send it a list that spreads the values through the inlets.

This is very useful if you want a Note-On message to trigger something in Pd but you don't want a Note-Off to trigger anything when you release the note.

INLET:

- 1st:

  - float - MIDI pitch.

- 2nd:

  - float - MIDI velocity (no output if equal to zero).

OUTLET:

- 1st:

  - float - MIDI pitch.

- 2nd:

  - float - MIDI velocity.

ARGUMENTS:

- NONE.
 


> see also [[makenote]](../makenote)

> updated for Pd version 0.28