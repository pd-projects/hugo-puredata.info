---
title: "[list prepend]"
description: "manipulate lists"
bref: "manipulate lists"
draft: false
categories: ["object", "General"]
---


### [list prepend]

Use list prepend to prepend a second list (defined via arguments or the right inlet) to the first list via the left inlet.

INLETS

- 1st:

  - anything - set messages to be prepended by a second list and output (a bang is a zero element list).

- 2nd:

  - anything - set messages to prepend to the first list (a bang is a zero element list and clears it).

OUTLET:

- list - the prepended list.

ARGUMENTS:

- list - initialize the list to prepend (default empty).

> see also [[list]](../list)\
> [[list append]](../list-append)\
> [[list store]](../list-store)\
> [[list split]](../list-split)\
> [[list trim]](../list-trim)\
> [[list length]](../list-length)\
> [[list fromsymbol]](../list-fromsymbol)\
> [[list tosymbol]](../list-tosymbol)