---
title: array quantile
description: outputs the specified quantile.
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
- array random
- array max
- array min
arguments:
- type: symbol
  description: array name if no flags are given (default none).
- type: float
  description: initial onset (default 0).
- type: float
  description: initial number of points (default -1, end of array).
flags:
- flag: -s <symbol, symbol>
  description: struct name and field name of main structure.
- flag: -f <symbol, symbol>
  description: struct name and field name of element structure.
inlets:
  1st:
    float: quantile (between 0 and 1).
  2nd:
    float: array onset (o is the end of array).
  3rd:
    float: number or points (-1 is the end of array).
  4th:
    pointer: pointer to the array if -s flag is used.
    symbol: set array name.
outlets:
  1st:
    float: random index value from the array.
draft: false
---
"array quantile" outputs the specified quantile by interpreting the array as a histogram. The output will always be in the range from 0 to "array size - 1". The 0.5 quantile is also known as the median. This generalizes the "array random" function allowing you to use the same source of randomness on several arrays, for example. Negative numbers in the array are silently replaced by zero. Quantiles outside the range 0-1 output the x values at the two extremes of the array (0 and 99 here).
