---
title: ftom
description: convert acoustical units
categories:
- object
pdcategory: Math
last_update: '0.40'
see_also:
- mtof~
- expr
inlets:
  1st:
    float: incomming value to be converted.
outlets:
  1st:
    float: converted value
draft: false
---
The mtof object transposes a midi value into a frequency in Hertz, so that "69" goes to "440". You can specify microtonal pitches as in "69.5", which is a quarter tone (or 50 cents) higher than 69 (so 0.01 = 1 cent). Ftom does the reverse. A frequency of zero Hertz is given a MIDI value of -1500 (strictly speaking, it is negative infinity.)
