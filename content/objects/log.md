---
title: log
description: math functions
categories:
- object
pdcategory: Math
see_also:
- +~
- +
- div
- expr
arguments:
- type: float
  description: initialize value of right inlet (default 0).
inlets:
  1st:
    bang: output the operation on the previously set values.
    float: value to the left side of operation and output.
  2nd:
    float: value to the right side of operation.
outlets:
  1st:
    float: the result of the operation.
draft: false
---
As in the signal version log~, log takes a base value via an argument or the right inlet, but it defaults to [e](https://en.wikipedia.org/wiki/E_(mathematical_constant)).
