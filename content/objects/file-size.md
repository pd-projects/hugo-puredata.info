---
title: file size
description: get size of a file
categories:
- object
pdcategory: Misc
last_update: '0.52'
see_also:
- text
- array
- list
- file
- file define
- file handle
- file mkdir
- file which
- file glob
- file stat
- file isfile
- file isdirectory
- file copy
- file move
- file delete
- file split
- file join
- file splitext
- file splitname
flags:
- flag: -q
  description: set quiet verbosity.
- flag: -v
  description: set loud verbosity.
inlets:
  1st:
    symbol: file or directory name.
    verbose <float>: set verbosity on or off.
outlets:
  1st:
    float: true <1> of false <0>.
  2nd:
    bang: if an error occurs.
draft: false
---

