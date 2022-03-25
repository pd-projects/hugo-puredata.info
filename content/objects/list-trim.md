---
title: list trim
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
- list length
- list fromsymbol
- list tosymbol
inlets:
  1st:
    list: list messages to be trimmed.
    symbol: the symbol selector is also trimmed.
    anything: any other messages are output intact.
outlets:
  1st:
    anything: trimmed list.
draft: false
pdcategory: General

---
Remove list selector.

The "list trim" object inputs lists (or makes lists out of incoming non-list messages) and outputs a message whose selector is the first item of the list, and whose arguments, if any, are the remainder of the list. If the list has no items, or if its first item is numeric, the selector is "list" (which might print out as list, float, or bang.)
