---
title: rmstodb
description: convert acoustical units
bref: convert acoustical units
categories:
- object
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
pdcategory: Math

---
The dbtorms and rmstodb objects convert from decibels to linear ("RMS") amplitude, so that 100 dB corresponds to an "RMS" of 1 Zero amplitude (strictly speaking, minus infinity dB) is clipped to zero dB, and zero dB, which should correspond to 0.0001 in "RMS", is instead rounded down to zero.
