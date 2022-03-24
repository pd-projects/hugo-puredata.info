---
title: "[random]"
description: "pseudo random integers"
bref: "pseudo random integers"
draft: false
categories: ["object"]
pd-category: "Math"
---

### [random]

Pseudo random integers.

Random outputs pseudo random integers from 0 to N-1 where N is the creation argument. You can specify a seed if you wish. Seeds are kept locally so that if two Randoms are seeded the same they will have the same output (or indeed you can seed the same one twice to repeat the output.)

On the other hand,  if you don't supply a seed each instance of random gets its own seed. WARNING: nothing is known about the quality of the pseudo random number generator. It isn't any standard one!

INLETS:

- 1st:

  - bang - generate a random integer number.

  - seed &lt;float&gt; - set a seed value for repeatable random numbers.

- 2nd:

  - float - set the range.

OUTLET:

- float - the generated random number.

ARGUMENT:

-  float - initial range value (default 1).

> see also [[expr]](../expr-family)
 
> updated for Pd version 0.33
