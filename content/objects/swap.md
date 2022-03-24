---
title: swap
description: swap two numbers
bref: swap two numbers
categories:
- object
last_update: '0.41'
arguments:
  float: initial right inlet value (default 0).
inlets:
  1st:
    bang: outputs the stored values swapped.
    float: set left value,  swap and output.
outlets:
  1st:
    float: value from left/1st inlet.
draft: false
pdcategory: General

---
The swap object swaps the positions of two incoming numbers. The number coming in through the right inlet will be sent to the left outlet and the number coming in left will come out right. Only the left inlet is hot and triggers output on both outlets. Output order is right to left as in [trigger].
