---
title: int
description: store and recall an integer
categories:
- object
last_update: '0.48'
see_also:
- float
- value
- send
arguments:
  float: initially stored value (default 0).
inlets:
  1st:
    bang: output the stored value.
    list: considers the first element if it's a float,  stores and outputs it.
    send <symbol>: send the stored value to a [receive] or [value] object that has
      the same name as the symbol (no output).
  2nd:
    float: store the value, non-integers are truncated (no output).
outlets:
  1st:
    float: the stored integer value.
pdcategory: General
aliases:
- i
draft: false

---
Truncate floats and store an integer

The int object stores a number initialized by its creation argument,  which may be reset using its inlet and output by sending it the "bang" message. Sending a number sets a new value and outputs it. A non-integer input is truncated to an integer (a la Max) so the object can also be used to truncate values and convert from float to integers.
