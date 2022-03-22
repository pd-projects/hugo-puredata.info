---
title: "[>], [>=], [<], [<=], [==], [!=], [&&], [||], [&], [|], [<<], [>>], [div], [mod]"
description: "other binary operators"
bref: "other binary operators"
draft: false
categories: ["object", "Math"]
---

### [>], [>=], [<], [<=], [==], [!=], [&&], [||], [&], [|], [&lt;&lt;], [&gt;&gt;], [div], [mod]

Other binary operators.

div and mod do integer division, where div outputs the integer quotient and mod outputs the remainder (modulus). In addition the "%" operator (provided for back compatibility) is like "mod" but acts differently for negative inputs (and might act variously depending on CPU design).

The bitwise operators "&" and "|" perform "and" and "or" on each bit of the inputs considered as binary numbers. the "&gt;&gt;" and "&lt;&lt;" objects perform left and right signed bit shifts. These also expect integer input and truncate float values.

Relational operators ('>' greater than, '==' equals, '!=' not equals etc.) output 1 or 0 depending on whether the relation is true or false. Unlike the previous ones, these can deal with float input.


INLETS:

- 1st:

  - bang - output the operation on the previously set values.

  - float - value to the left side of operation and output.

- 2nd:

  - float - value to the right side of operation.

OUTLET:

- float - the result of the operation.

ARGUMENT:

- float - initialize value of right inlet (default 0).

> see also [[+~]](../#) (etc) - binary signal operators

> [[expr]](../expr-family) - evaluation expressions

> [[sin]](../math-functions) [[log]](../math-functions) (etc) - math functions

> Updated for Pd version 0.47
 