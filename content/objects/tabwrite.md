---
title: "[tabwrite]"
description: "write a number to a table"
bref: "write a number to a table"
draft: false
categories: ["object"]
pdcategory: "Arrays & Tables"
---

### [tabwrite]

Tabwrite writes floats into an array,  input values are set in the left inlet,  while the index is set on the right inlet.


INLET:

- 1st:

  - float - sets index value and write to a table.

  - set &lt;symbol&gt; - set the table name.

- 2nd:

  - float - sets index to write to.

OUTLETS:

- NONE.

ARGUMENT:

- symbol - sets table name with the sample.
 
> see also [[array]](../array) [[tabread]](../tabread) [[tabread4]](../tabread4) [[tabwrite~]](../tabwrite~)

> and Pd's:

> `doc/2.control.examples/15.array.pd`

> `doc/2.control.examples/16.more.arrays.pd`
 
> updated for Pd version 0.33
 
