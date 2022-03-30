---
title: list trim
description: manipulate lists
categories:
- object
pdcategory: General
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
    anything: any other messages are output intact.
    list: list messages to be trimmed.
    symbol: the symbol selector is also trimmed.
outlets:
  1st:
    anything: trimmed list.
draft: false
---
Remove list selector.

The "list trim" object inputs lists (or makes lists out of incoming non-list messages) and outputs a message whose selector is the first item of the list, and whose arguments, if any, are the remainder of the list. If the list has no items, or if its first item is numeric, the selector is "list" (which might print out as list, float, or bang.)
