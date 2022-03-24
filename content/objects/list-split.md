---
title: list split
description: manipulate lists
bref: manipulate lists
categories:
- object
see_also:
- list
- list append
- list prepend
- list store
- list trim
- list length
- list fromsymbol
- list tosymbol
arguments:
  float: initialize split point.
inlets:
  1st: {}
outlets:
  1st:
    list: if incoming list is shorter than n.
draft: false
pdcategory: General

---
Cut a list into smaller ones.

The "list split" object takes lists and outputs the first "n" items (left outlet) and the remaining ones (middle outlet). If the incoming list also has 'n' items, the middle outlet spits a list with zero elements (which becomes a bang). The two outputs appear in the usual right-to-left order. In case there are fewer than "n" items in the list, it is output (in its entirety) from the third outlet instead. The creation argument or the inlet sets the split point.

INLETS

- 1st:

  - anything - messages to be split into smaller lists.

- 2nd:

  - float - sets new 'n' split point.
