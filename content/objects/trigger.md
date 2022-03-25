---
title: trigger
description: sequence messages in right-to-left order.
categories:
- object
last_update: '0.52'
see_also:
- bang
- unpack
arguments:
  list: 'symbols that define outlet''s message type: float'',  ''bang'',  ''symbol'',  ''list'',  ''anything''
    and ''pointer'',  all of which can be abreviatted (default: f f).'
inlets:
  1st:
    anything: any message to be sequenced over the outlets.
outlets:
  'n: (depends on the number of arguments)':
    anything: sequenced messages from right to left,  the number of outlets and message
      type depends on the arguments.
draft: false
pdcategory: General
aliases:
- t

---
The trigger object outputs its input from right to left. Because of the hot/cold inlet paradigm of Pd, output from right to left is the usual output order in Pd objects.

The creation arguments specify the number of outlets and message type to output. Most of the time you want to match the input message type to the argument, but a mix is possible and can be convenient.

The message types/arguments are: 'float', 'bang', 'symbol', 'list', 'anything' and 'pointer' (see [pd pointer]) - all of which can be abbreviated to its first letter like the object itself.

`[trigger float bang symbol list anything pointer]` same as: `[t f b s l a p]`
