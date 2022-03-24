---
title: "[list append]"
description: "manipulate lists"
bref: "manipulate lists"
draft: false
categories: ["object"]
pdcategory: "General"
aliases: ["list"]
---

### [list append]

Use list append to concatenate a second list (defined via arguments or the right inlet) to the first list via the left inlet.

INLETS

- 1st:

  - anything - set messages to concatenate to a second list and output (a bang is a zero element list).

- 2nd:

  - anything - set messages to append to the first list (a bang is a zero element list and clears it).

OUTLET:

- list - the concatenated list.

ARGUMENTS:

- list - initialize the list to append (default empty).

> see also [[list]](../list)\
> [[list prepend]](../list-prepend)\
> [[list store]](../list-store)\
> [[list split]](../list-split)\
> [[list trim]](../list-trim)\
> [[list length]](../list-length)\
> [[list fromsymbol]](../list-fromsymbol)\
> [[list tosymbol]](../list-tosymbol)
