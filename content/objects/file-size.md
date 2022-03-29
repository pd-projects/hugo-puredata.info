---
title: file size
description: get size of a file
categories:
- object
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
inlets:
  1st: 
    symbol: file or directory name.
    verbose <float>: set verbosity on or off.
outlets:
  1st:
    float: true <1> of false <0>.
  2nd:
    bang: if an error occurs.

flags:
  -q: set quiet verbosity.
  -v: set loud verbosity.

draft: false
pdcategory: Misc

---



