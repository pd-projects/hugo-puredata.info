---
title: "[mod]"
description: "higher math"
bref: "higher math"
draft: false
categories: ["object"]
pdcategory: "Math"
---

### [mod]

div and mod do integer division, where div outputs the integer quotient and mod outputs the remainder (modulus). In addition the "%" operator (provided for back compatibility) is like "mod" but acts differently for negative inputs (and might act variously depending on CPU design).

INLETS:

- 1st:

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
 
