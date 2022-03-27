---
title: array
description: general array creation and manipulation
categories:
- object
last_update: '0.52'
see_also:
- array define
- array size
- array sum
- array get
- array set
- array quantile
- array random
- array max
- array min
inlets:
  1st: {}
outlets:
  1st: {}
arguments:
  symbol: 'sets the function of [array], possible values: define, size, sum, get, set, quantile, random, max and min. The default value is "define".'
draft: false
pdcategory: Arrays & Tables

---

In Pd an array may be part of a "garray" (a graphical array of numbers) or appear as a slot in a data structure (in which case the elements may be arbitrary data, not necessarily just numbers). The "array" object can define an array (so far just of numbers but maybe later arbitrary data structures) or access an array defined elsewhere to get or change its size, set or read its elements, and so on.