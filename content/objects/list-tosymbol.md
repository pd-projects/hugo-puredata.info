---
title: list tosymbol
description: manipulate lists
bref: manipulate lists
categories:
- object
see_also:
- list
- list append
- list prepend
- list store
- list split
- list trim
- list length
- list fromsymbol
inlets:
  1st: 
   list: list of character codes to convert to a symbol.
outlets:
  1st:
    symbol: converted symbol from list of character codes.
draft: false
pdcategory: General

---
Convert from list of numeric character codes to symbols.

`[list fromsymbol]` and `[list tosymbol]` allow you to do string manipulations (such as scanning a filename for '/' characters). They convert a list of numbers (which might be ASCII or might be unicode if, for example, they represent a filename on a non-ASCII machine) to or from a symbol.

