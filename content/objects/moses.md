---
title: moses
description: part a numeric stream
categories:
- object
last_update: '0.33'
see_also:
- change
- select
arguments:
  float: set initial control value (default 0).
inlets:
  1st:
    float: number to be parted.
  2nd:
    float: set control value.
outlets:
  1st:
    float: input number if less than control value.
  2nd:
    float: input number if equal or higher than control value.
draft: false
pdcategory: General

---
Moses takes numbers and outputs them at left if they're less than a control value,  and at right if they're greater or equal to it.
