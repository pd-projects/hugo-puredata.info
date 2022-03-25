---
title: route
description: route messages according to first element
categories:
- object
last_update: '0.43'
see_also:
- select
arguments:
  list: of floats or symbols to route to to (default 0).
inlets:
  1st:
    anything: any message to route according to the first element.
  2nd:
    float/symbol: if there's one argument,  an inlet is created to update it.
outlets:
  'n: (depends on the number of arguments)':
    anything: routed message with the first element trimmed.
  rightmost:
    anything: when input doesn't match the arguments,  it is passed here.
draft: false
pdcategory: General

---
Route checks the first element of a message against each of its arguments,  which may be numbers or symbols (but not a mixture of the two). If a match is found,  the rest of the message appears on the corresponding outlet. If there's no match,  the message is repeated to the last "rejection" outlet. The number of outlets is the number of arguments plus one.

If no argument is given,  [route] loads a float argument of 0 and creates a second inlet so you can change the argument value (to another float). In the same way,  a single symbol argument adds an inlet that expects a symbol message to change the argument.
