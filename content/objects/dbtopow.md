---
title: dbtopow
description: convert acoustical units
categories:
- object
pdcategory: Math
last_update: '0.40'
see_also:
- mtof~
- expr
inlets:
  1st:
    float: incomming value to be converted.
outlets:
  1st:
    float: converted value
draft: false
---
dbtopow and powtodb convert decibels to and from power units, equal to the square of the "RMS" amplitude.
