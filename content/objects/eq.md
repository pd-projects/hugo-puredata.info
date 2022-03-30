---
title: ==
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
- description: initialize value of right inlet (default 0).
  type: float
inlets:
  1st:
  - type: bang
    description: output the operation on the previously set values.
  - type: float
    description: value to the left side of operation and output.
  2nd:
  - type: float
    description: value to the right side of operation.
outlets:
  1st:
  - type: float
    description: the result of the operation.
draft: false
---
Relational operators ('>' greater than, '==' equals, '!=' not equals etc.) output 1 or 0 depending on whether the relation is true or false.
