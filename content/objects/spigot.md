---
title: spigot
description: pass or block messages
categories:
- object
last_update: '0.38'
arguments:
  float: initialize right inlet.
inlets:
  1st:
    anything: any message to pass or not.
  2nd:
    float: nonzero to pass messages,  zero to stop them.
outlets:
  1st:
    anything: any input message if spigot is openned.
draft: false
pdcategory: General

---
Spigot passes messages from its left inlet to its outlet,  as long as a nonzero number is sent to its right inlet. When its right inlet gets zero,  incoming messages are "blocked" i.e.,  ignored.
