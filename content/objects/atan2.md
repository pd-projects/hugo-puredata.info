---
title: "[atan2]"
description: "trigonometric functions"
bref: "trigonometric functions"
draft: false
categories: ["object"]
pd-category: "Math"
---

### [atan2]

The atan2 version takes an (x, y) pair and gives you an output between -pi and pi, it also takes a bang message in the left inlet to evaluate the operation with the previously set values.

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

> see also [[+~]](../plus~) (etc) - signal versions

> [[+]](../plus) (etc) - binary arithmetic operators

> [[div]](../div) (etc) - other binary operators

> [[expr]](../expr-family) - evaluation expressions

> Updated for Pd version 0.52
 
