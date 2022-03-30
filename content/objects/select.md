---
title: select
description: test for matching numbers or symbols
categories:
- object
pdcategory: General
last_update: '0.33'
see_also:
- route
arguments:
- type: list
  description: of floats or symbols to match to (default 0).
inlets:
  1st:
    float/symbol: input to compare to arguments.
  2nd:
    float/symbol: if there's one argument,  an inlet is created to update it.
outlets:
  'n: (depends on the number of arguments)':
    bang: when the input matches an argument that corresponds to the outlet.
  rightmost:
    float/symbol: when input doesn't match the arguments,  it is passed here.
draft: false
aliases:
- sel
---

