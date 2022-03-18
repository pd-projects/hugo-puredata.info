---
title: "[until]"
description: "looping mechanism"
bref: "looping mechanism"
draft: false
categories: ["object", "General"]
---

### [until]

Looping mechanism.

The until object's left inlet starts a loop in which it outputs "bang" until its right inlet gets a bang which stops it. If you start "until" with a number,  it iterates at most that number of times,  as in the Max "uzi" object.


INLET:

- 1st:

  - float - set number of iterations in the loop.

  - bang - start loop until a bang reaches the right inlet.

- 2nd:

  - bang - stops the loop.

OUTLET:

- bang - bangs in a loop.

ARGUMENT:

- NONE
 

 
> updated for Pd version 0.28