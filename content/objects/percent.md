---
title: '%'
description: higher math
bref: higher math
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
div and mod do integer division, where div outputs the integer quotient and mod outputs the remainder (modulus). In addition the "%" operator (provided for back compatibility) is like "mod" but acts differently for negative inputs (and might act variously depending on CPU design).
