---
title: "[log]"
description: "math functions"
bref: "math functions"
draft: false
categories: ["object"]
pd-category: "Math"
---

### [log]

As in the signal version log~, log takes a base value via an argument or the right inlet, but it defaults to “e”.


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
 
