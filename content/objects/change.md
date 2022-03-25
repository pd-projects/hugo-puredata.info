---
title: change
description: remove repeated numbers from a stream
categories:
- object
last_update: '0.27'
arguments:
  float: initial value (default 0).
inlets:
  1st:
    bang: output current value.
    float: input value (repeated numbers are filtered).
    set <float>: set the value.
outlets:
  1st:
    float: unrepeated value.
draft: false
pdcategory: General

---
The change object outputs its input only when it changes. You can "set" the current value,  or bang to force output.
