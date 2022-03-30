---
title: array sum
description: sum all or a range of elements.
categories:
- object
pdcategory: Arrays & Tables
last_update: '0.52'
see_also:
- array
- array define
- array size
- array get
- array set
- array quantile
- array random
- array max
- array min
arguments:
- type: 1) symbol
  description: array name if no flags are given (default none).
- type: 2) float
  description: initial onset (default 0).
- type: 3) float
  description: initial number of points (default -1, end of array).
flags:
- flag: -s <symbol, symbol>
  description: struct name and field name of main structure.
- flag: -f <symbol, symbol>
  description: struct name and field name of element structure.
inlets:
  1st:
    bang: output sum.
    float: onset (index to sum from, 0 is the start).
  2nd:
    float: number or points to sum from onset (-1 is the end of array).
  3rd:
    pointer: pointer to the array if -s flag is used.
    symbol: set array name.
outlets:
  1st:
    float: array size.
draft: false
---
"array sum" outputs the sum of all or a selected range of elements of the array.
