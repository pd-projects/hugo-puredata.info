---
title: "[rmstodb]"
description: "convert acoustical units"
bref: "convert acoustical units"
draft: false
categories: ["object"]
pdcategory: "Math"
---

### [rmstodb]

The dbtorms and rmstodb objects convert from decibels to linear ("RMS") amplitude, so that 100 dB corresponds to an "RMS" of 1 Zero amplitude (strictly speaking, minus infinity dB) is clipped to zero dB, and zero dB, which should correspond to 0.0001 in "RMS", is instead rounded down to zero.

INLET:

- float - incomming value to be converted.

OUTLET:

- float - converted value

ARGUMENT:

- NONE.
 


> see also [[mtof~]](../#) (etc.) - acoustic conversions for audio signals

> [[expr]](../expr-family) - evaluation expressions
 
 
> updated for Pd version 0.40
 
