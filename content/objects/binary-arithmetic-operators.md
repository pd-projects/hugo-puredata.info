---
title: "[+] [-] [*] [/] [max] [min]"
description: "arithmetic"
bref: "arithmetic"
draft: false
categories: ["object"]
pd-category: "Math"
---

### [+], [-], [*], [/], [max], [min]

Binary arithmetic operators.

The arithmetic binary operators perform the 4 arithmetic functions (+,  etc) or output the minimum or maximum of two numbers (min,  max). All of these objects take a bang message to evaluate the operation with the previously set values.

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

> [[div]](../#) [[>]](../#) [[&&]](../#) (etc) - other binary operators

> [[sin]](../sin) [[log]](../#) (etc) - math functions

> [[expr]](../expr-family) - evaluation expressions
 
 
> updated for Pd version 0.47
