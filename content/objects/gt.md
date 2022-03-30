---
title: '>'
description: relational tests
categories:
- object
pdcategory: Math
see_also:
- +~
- expr
- sin
- log
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
Relational operators ('>' greater than, '==' equals, '!=' not equals etc.) output 1 or 0 depending on whether the relation is true or false.
