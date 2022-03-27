---
title: until
description: looping mechanism
categories:
- object
last_update: '0.28'
inlets:
  1st:
    bang: stops the loop.
    float: set number of iterations in the loop.
  2nd:
    bang: stops the loop.
outlets:
  1st:
    bang: bangs in a loop.
draft: false
pdcategory: General

---
The until object's left inlet starts a loop in which it outputs "bang" until its right inlet gets a bang which stops it. If you start "until" with a number,  it iterates at most that number of times,  as in the Max "uzi" object.
