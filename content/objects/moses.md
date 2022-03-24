---
title: "[moses]"
description: "part a numeric stream"
bref: "part a numeric stream"
draft: false
categories: ["object"]
pdcategory: "General"
---

### [moses]

Part a numeric stream

Moses takes numbers and outputs them at left if they're less than a control value,  and at right if they're greater or equal to it.

INLETS:

- 1st:

  - float - number to be parted.

- 2nd:

  - float - set control value.

OUTLETS:

- 1st:

  - float - input number if less than control value.

- 2nd:

  - float - input number if equal or higher than control value.

ARGUMENT:

- float - set initial control value (default 0).
 
 
> see also [[change]](../change) [[select]](../select) 
 
> updated for Pd version 0.33