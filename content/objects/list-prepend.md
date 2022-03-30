---
title: list prepend
description: manipulate lists
categories:
- object
pdcategory: General
see_also:
- list
- list append
- list store
- list split
- list trim
- list length
- list fromsymbol
- list tosymbol
arguments:
- type: list
  description: initialize the list to prepend (default empty).
inlets:
  1st:
    anything: set messages to be prepended by a second list and output (a bang is
      a zero element list).
  2nd:
    anything: set messages to prepend to the first list (a bang is a zero element
      list and clears it).
outlets:
  1st:
    list: the prepended list.
draft: false
---
Use list prepend to concatenate a second list (defined via arguments or the right inlet) to the first list via the left inlet.
