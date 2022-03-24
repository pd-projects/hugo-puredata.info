---
title: sin], [cos], [tan], [atan], [atan2], [wrap], [abs], [sqrt], [exp], [log], [pow
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
  bang: output the operation on the previously set values.
  float: initialize value of right inlet (default 0).
inlets:
  1st:
    float: input value to given function.
outlets:
  1st:
    float: the result of the operation.
draft: false
pdcategory: Math

---
Unlike the signal version cos~, control-rate trigonometric functions take inputs in radians.

The arc tangent takes two forms. The atan2 version takes an (x, y) pair and gives you an output between -pi and pi, it also takes a bang message in the left inlet to evaluate the operation with the previously set values.

We also have wrap, absolute value, square root, exponential, logarithms and power, all of which have corresponding signal versions. The "wrap" object wraps the input to a value between 0 and 1, including negative numbers (for instance, -0.2 maps to 0.8.). As in the signal version log~, log takes a base value via an argument or the right inlet, but it defaults to "e". Pow raises a number on the left inlet to a numeric power (given by the right inlet or argument) - like the signal version, pow has protection against NaNs (they become 0).




------------------------
