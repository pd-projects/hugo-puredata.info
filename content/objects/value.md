---
title: "[value]"
description: "shared numeric value"
bref: "shared numeric value"
draft: false
categories: ["object"]
pd-category: "General"
---

### [value]

Shared numeric value

"Value" stores a numeric value which is shared between all values with the same name (which need not be in the same Pd window.)

The value may also be stored or recalled in expressions via the expr, expr~, and fexpr~ objects.

The value object can also receive float values sent via a [send] object or a message if it has a variable with the same name.


INLETS:

- 1st:

  - float - sets variable value.

  - bang - outputs the value.

  - send &lt;symbol&gt; - sends the value to a matching receive name.

- 2nd: (if created without argument)

  - symbol - sets the value name.

OUTLET:

- float - sets variable value.

ARGUMENT:

- symbol - sets value name (if no name is given,  a right inlet is created to set the name).


 
> see also [[send]](../send) [[int]](../int) [[float]](../float) [[expr]](../expr)
 
> updated for Pd version 0.51.