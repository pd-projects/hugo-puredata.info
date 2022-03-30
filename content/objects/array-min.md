---
title: array min
description: output minimum value of an array.
categories:
- object
pdcategory: Arrays & Tables
last_update: '0.52'
see_also:
- array
- array define
- array size
- array sum
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
    bang: to find min
    float: onset (index to output from, 0 is the start).
  2nd:
    float: number or points to output from onset (-1 is the end of array).
  3rd:
    pointer: pointer to the array if -s flag is used.
    symbol: set array name.
outlets:
  1st:
    float: minimum value
  2nd:
    float: index of found value
draft: false
---
"array min" find the minimum value in the array. The first outlet is the value and the second is the index (the x location where the value was found). The search may be restricted to a sub-domain of the array by specifying the "onset" and "number of points".
