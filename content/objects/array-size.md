---
title: array size
description: output or set array size.
categories:
- object
pdcategory: Arrays & Tables
last_update: '0.52'
see_also:
- array
- array define
- array sum
- array get
- array set
- array quantile
- array random
- array max
- array min
arguments:
- type: 1) symbol
  description: array name if no flags are given (default = none).
flags:
- flag: -s <symbol, symbol>
  description: struct name and field name of main structure.
- flag: -f <symbol, symbol>
  description: struct name and field name of element structure.
inlets:
  1st:
    bang: output the array size.
    float: set the array size.
  2nd:
    pointer: pointer to the array if '-s' flag is used.
    symbol: set array name.
outlets:
  1st:
    float: array size.
draft: false
---
"array define" maintains an array and can name it so that other objects can find it (and later should have some alternative, anonymous way to be found).
