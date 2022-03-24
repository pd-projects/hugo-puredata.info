---
title: "[swap]"
description: "swap two numbers"
bref: "swap two numbers"
draft: false
categories: ["object"]
pdcategory: "General"
---

### [swap]

Swap two numbers

The swap object swaps the positions of two incoming numbers. The number coming in through the right inlet will be sent to the left outlet and the number coming in left will come out right. Only the left inlet is hot and triggers output on both outlets. Output order is right to left as in [trigger].

INLET:

- 1st:

  - bang - outputs the stored values swapped.

  - float - set left value,  swap and output.

- 2nd:

  - float - set left value,  swap and output.

OUTLET:

- 1st:

  - float - value from right/2nd inlet.

- 2nd:

  - float - value from left/1st inlet.

ARGUMENT:

- float - initial right inlet value (default 0).
 
> updated for Pd version 0.41