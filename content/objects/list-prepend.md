---
title: list prepend
description: manipulate lists
categories:
- object
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
  list: initialize the list to prepend (default empty).
inlets:
  1st:
    anything: set messages to be prepended by a second list and output (a bang is a zero element list).
  2nd:
    anything: set messages to prepend to the first list (a bang is a zero element list and clears it).
outlets:
  1st:
    list: the prepended list.
draft: false
pdcategory: General

---
Use list prepend to prepend a second list (defined via arguments or the right inlet) to the first list via the left inlet.
