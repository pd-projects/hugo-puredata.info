---
title: "[list]"
description: "manipulate lists"
bref: "manipulate lists"
draft: false
categories: ["object"]
pd-category: "General"
---

### [list]

Manipulate lists.

Short for "list append"

INLETS

- 1st:

  - anything - set messages to concatenate to a second list and output (a bang is a zero element list).

- 2nd:

  - anything - set messages to append to the first list (a bang is a zero element list and clears it).

OUTLET:

- list - the concatenated list.

ARGUMENTS:

- symbol - sets the function of [list], possible values: append, prepend, store, split, trim, length, fromsymbol and tosymbol. The default value is 'append'.

> see also [[list append]](../list-append)\
> [[list prepend]](../list-prepend)\
> [[list store]](../list-store)\
> [[list split]](../list-split)\
> [[list trim]](../list-trim)\
> [[list length]](../list-length)\
> [[list fromsymbol]](../list-fromsymbol)\
> [[list tosymbol]](../list-tosymbol)


