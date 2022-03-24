---
title: "[list trim]"
description: "manipulate lists"
bref: "manipulate lists"
draft: false
categories: ["object"]
pd-category: "General"
---



### [list trim]

Remove list selector.

The "list trim" object inputs lists (or makes lists out of incoming non-list messages) and outputs a message whose selector is the first item of the list, and whose arguments, if any, are the remainder of the list. If the list has no items, or if its first item is numeric, the selector is "list" (which might print out as list, float, or bang.)

INLETS

- list - list messages to be trimmed.

- symbol - the symbol selector is also trimmed.

- anything - any other messages are output intact.

OUTLET:

- anything - trimmed list.


ARGUMENTS:

- NONE.

> see also [[list]](../list)\
> [[list append]](../list-append)\
> [[list prepend]](../list-prepend)\
> [[list store]](../list-store)\
> [[list split]](../list-split)\
> [[list length]](../list-length)\
> [[list fromsymbol]](../list-fromsymbol)\
> [[list tosymbol]](../list-tosymbol)
