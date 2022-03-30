---
title: array quantile
description: outputs the specified quantile.
categories:
- object
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
inlets:
  1st:
    float: quantile (between 0 and 1).
  2nd:
   float: array onset (o is the end of array).
  3rd:
    float: number or points (-1 is the end of array).
  4th:
    symbol: set array name.
    pointer: pointer to the array if -s flag is used.
outlets:
  1st:
    float: random index value from the array.
arguments:
  1) symbol: array name if no flags are given (default none).
  2) float: initial onset (default 0).
  3) float: initial number of points (default -1, end of array).

flags:
  -s <symbol, symbol>: struct name and field name of main structure.
  -f <symbol, symbol>: struct name and field name of element structure.
draft: false
pdcategory: Arrays & Tables

---

"array quantile" outputs the specified quantile by interpreting the array as a histogram. The output will always be in the range from 0 to "array size - 1". The 0.5 quantile is also known as the median. This generalizes the "array random" function allowing you to use the same source of randomness on several arrays, for example. Negative numbers in the array are silently replaced by zero. Quantiles outside the range 0-1 output the x values at the two extremes of the array (0 and 99 here).
