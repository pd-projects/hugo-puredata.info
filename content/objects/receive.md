---
title: receive
description: Receive messages without patch cords.
bref: Receive messages without patch cords.
categories:
- object
last_update: '0.48'
see_also:
- send~
- receive~
- samplerate~
arguments:
  symbol: 'receive name symbol (default: empty symbol)'
outlets:
  1st:
    any message: outputs the messages destined to its receive name.
pdcategory: General
aliases:
- r
draft: false

---
The [receive] object gets messages directly from [send] or other objects like [list store], [float], [int] and [value] via a `send` method.
