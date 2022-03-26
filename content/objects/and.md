---
title: '&'
description: bit twiddling
categories:
- object
see_also:
- +~
- expr
- sin
- log
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
The bitwise operators "&" and "|" perform "and" and "or" on each bit of the inputs considered as binary numbers. the "&gt;&gt;" and "&lt;&lt;" objects perform left and right signed bit shifts. These also expect integer input and truncate float values.
