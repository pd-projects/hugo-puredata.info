---
title: array size
description: output or set array size.
categories:
- object
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
inlets:
  1st:
    bang: output the array size.
    float: set the array size.
  2nd:
    symbol: set array name.
    pointer: pointer to the array if '-s' flag is used.
outlets:
  1st:
    float: array size.
arguments:
  1) symbol: array name if no flags are given (default = none).

flags:
  -s <symbol, symbol>: struct name and field name of main structure.
  -f <symbol, symbol>: struct name and field name of element structure.
draft: false
pdcategory: Arrays & Tables

---

"array define" maintains an array and can name it so that other objects can find it (and later should have some alternative, anonymous way to be found).
