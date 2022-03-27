---
title: loadbang
description: bang on load
categories:
- object
last_update: '0.47'
see_also:
- bang
outlets:
  1st: 
    bang: when loadding the patch.
draft: false
pdcategory: Misc

---

The loadbang object outputs a 'bang' message when the containing patch is opened as a document or included in another patch as an abstraction.

Loadbangs within abstractions send their "bang" messages before those of loadbangs in the calling patch. Otherwise, the order in which the "bangs" are sent from two loadbang objects is undefined.

You can force loaddbangs to fire if you send a 'loadbang' message to the patch (see 'pd-messages').

