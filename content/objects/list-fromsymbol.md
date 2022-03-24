---
title: "[list fromsymbol]"
description: "manipulate lists"
bref: "manipulate lists"
draft: false
categories: ["object", "General"]
---

### [list fromsymbol]

Convert from symbols to lists of numeric character codes.

`[list fromsymbol]` and `[list tosymbol]` allow you to do string manipulations (such as scanning a filename for '/' characters). They convert a list of numbers (which might be ASCII or might be unicode if, for example, they represent a filename on a non-ASCII machine) to or from a symbol.

INLETS

- symbol - symbol to be converted to a list of character codes.

OUTLET:

- list - list of converted character codes.

ARGUMENTS:

- NONE.

> see also [[list]](../list)\
> [[list append]](../list-append)\
> [[list prepend]](../list-prepend)\
> [[list store]](../list-store)\
> [[list split]](../list-split)\
> [[list trim]](../list-trim)\
> [[list length]](../list-length)\
> [[list tosymbol]](../list-tosymbol)