---
title: wrap
description: wrap a number to range [[0, 1)
bref: wrap a number to range [[0, 1)
categories:
- object
see_also:
- +~
- +
- div
- expr
inlets:
  1st:
    float: input value to given function.
outlets:
  1st:
    float: the result of the operation.
draft: false
pdcategory: Math

---
The "wrap" object wraps the input to a value between 0 and 1, including negative numbers (for instance, -0.2 maps to 0.8.).
