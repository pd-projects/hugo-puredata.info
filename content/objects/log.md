---
title: log
description: math functions
bref: math functions
categories:
- object
see_also:
- +~
- +
- div
- expr
arguments:
  float: initialize value of right inlet (default 0).
inlets:
  2nd:
    float: value to the right side of operation.
  float - input value to given function.:
    bang: output the operation on the previously set values.
    float: value to the left side of operation and output.
outlets:
  1st:
    float: the result of the operation.
draft: false
pdcategory: Math

---
As in the signal version log~, log takes a base value via an argument or the right inlet, but it defaults to “e”.
