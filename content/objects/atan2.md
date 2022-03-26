---
title: atan2
description: trigonometric functions
bref: trigonometric functions
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
  1st:
    bang: output the operation on the previously set values.
    float: value to the left side of operation and output.
  2nd:
    float: value to the right side of operation.
outlets:
  1st:
    float: the result of the operation.
draft: false
pdcategory: Math

---
The atan2 version takes an (x, y) pair and gives you an output between -pi and pi, it also takes a bang message in the left inlet to evaluate the operation with the previously set values.
