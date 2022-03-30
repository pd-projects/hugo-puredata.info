---
title: file copy
description: copy a file around.
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
- file size
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
    list: source and destination.
    verbose <float>: set verbosity on or off.
outlets:
  1st:
    list: source and destination on success.
  2nd:
    bang: if an error occurs.
draft: false
---
[file copy] duplicates the content of a file to a destination.
