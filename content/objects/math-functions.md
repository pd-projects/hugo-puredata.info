---
title: "[sin], [cos], [tan], [atan], [atan2], [wrap], [abs], [sqrt], [exp], [log], [pow]"
description: "math functions"
bref: "math functions"
draft: false
categories: ["object", "Math"]
---

### [sin], [cos], [tan], [atan], [atan2], [wrap], [abs], [sqrt], [exp], [log], [pow]

Math functions.

Unlike the signal version cos~, control-rate trigonometric functions take inputs in radians.

The arc tangent takes two forms. The atan2 version takes an (x, y) pair and gives you an output between -pi and pi, it also takes a bang message in the left inlet to evaluate the operation with the previously set values.

We also have wrap, absolute value, square root, exponential, logarithms and power, all of which have corresponding signal versions. The "wrap" object wraps the input to a value between 0 and 1, including negative numbers (for instance, -0.2 maps to 0.8.). As in the signal version log~, log takes a base value via an argument or the right inlet, but it defaults to "e". Pow raises a number on the left inlet to a numeric power (given by the right inlet or argument) - like the signal version, pow has protection against NaNs (they become 0).




------------------------
INLET:

- float - input value to given function.

OUTLET:

- float - the result of the operation.

ARGUMENT:

- NONE.

--------------------------

**[atan2], [log], [pow]*** - math functions (two inlets)

INLETS:

- float - input value to given function.

  - bang - output the operation on the previously set values.

  - float - value to the left side of operation and output.

- 2nd:

  - float - value to the right side of operation.

OUTLET:

- float - the result of the operation.

ARGUMENT:

- float - initialize value of right inlet (default 0).

-------------------------

 

> see also [[+~]](../#) (etc) - signal versions

> [[+]](../binary-arithmetic-operators) (etc) - binary arithmetic operators

> [[div]](../other-binary-operators) (etc) - other binary operators

> [[expr]](../expr-family) - evaluation expressions

> Updated for Pd version 0.52
 
