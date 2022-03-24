---
title: "[select]"
description: "test for matching numbers or symbols"
bref: "test for matching numbers or symbols"
draft: false
categories: ["object"]
pd-category: "General"
---

### [select]

Test for matching numbers or symbols.

INLETS:

- 1st:

  - float/symbol - input to compare to arguments.

- 2nd:

  - float/symbol - if there's one argument,  an inlet is created to update it.

OUTLETS:

- n: (depends on the number of arguments)

  - bang - when the input matches an argument that corresponds to the outlet.

- rightmost:

  - float/symbol - when input doesn't match the arguments,  it is passed here.

ARGUMENTS:

  - list - of floats or symbols to match to (default 0).

> see also [[route]](../route)  

> updated for Pd version 0.33