---
title: "[clip]"
description: "force a number into a range"
bref: "force a number into a range"
draft: false
categories: ["object"]
pdcategory: "Math"
---

### [clip]

Bound a number between two limits.

The clip object passes its signal input to its output,  clipping it to lie between two limits.

INLETS:

- 1st:

  - float - number to clip.

  - bang - re clip last incomming number between the two limits.

- 2nd:

  - float - set lower limit.

- 3rd:

  - float - set upper limit.

OUTLET:

- float - the clipped value.

ARGUMENT:

- 1st float - initial lower limit (default 0).

- 2nd float - initial upper limit (default 0).

> see also [[clip~]](../clip~) [[expr]](../expr-family) [[max]](../max) [[min]](../min)

> updated for Pd version 0.47
 
