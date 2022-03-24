---
title: "[ftom]"
description: "convert acoustical units"
bref: "convert acoustical units"
draft: false
categories: ["object"]
pd-category: "Math"
---

### [ftom]

The mtof object transposes a midi value into a frequency in Hertz, so that "69" goes to "440". You can specify microtonal pitches as in "69.5", which is a quarter tone (or 50 cents) higher than 69 (so 0.01 = 1 cent). Ftom does the reverse. A frequency of zero Hertz is given a MIDI value of -1500 (strictly speaking, it is negative infinity.)

INLET:

- float - incomming value to be converted.

OUTLET:

- float - converted value

ARGUMENT:

- NONE.
 


> see also [[mtof~]](../#) (etc.) - acoustic conversions for audio signals

> [[expr]](../expr-family) - evaluation expressions
 
 
> updated for Pd version 0.40
 
