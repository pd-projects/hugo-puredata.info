---
title: "[||]"
description: "bit twiddling"
bref: "bit twiddling"
draft: false
categories: ["object"]
pdcategory: "Math"
---

### [||]

The bitwise operators "&" and "|" perform "and" and "or" on each bit of the inputs considered as binary numbers. the "&gt;&gt;" and "&lt;&lt;" objects perform left and right signed bit shifts. These also expect integer input and truncate float values.

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

> see also [[+~]](../#) (etc) - binary signal operators

> [[expr]](../expr-family) - evaluation expressions

> [[sin]](../#) [[log]](../#) (etc) - math functions

> Updated for Pd version 0.47
 
