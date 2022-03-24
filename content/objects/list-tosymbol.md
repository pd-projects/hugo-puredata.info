---
title: "[list tosymbol]"
description: "manipulate lists"
bref: "manipulate lists"
draft: false
categories: ["object"]
pd-category: "General"
---


### [list tosymbol]

Convert from list of numeric character codes to symbols.

`[list fromsymbol]` and `[list tosymbol]` allow you to do string manipulations (such as scanning a filename for '/' characters). They convert a list of numbers (which might be ASCII or might be unicode if, for example, they represent a filename on a non-ASCII machine) to or from a symbol.

INLETS

- list - list of character codes to convert to a symbol.

OUTLET:

- symbol - converted symbol from list of character codes.

ARGUMENTS:

- NONE.

> see also [[list]](../list)\
> [[list append]](../list-append)\
> [[list prepend]](../list-prepend)\
> [[list store]](../list-store)\
> [[list split]](../list-split)\
> [[list trim]](../list-trim)\
> [[list length]](../list-length)\
> [[list fromsymbol]](../list-fromsymbol)
