---
title: file move
description: move a file to a new destination.
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
- file size
- file copy
- file delete
- file split
- file join
- file splitext
- file splitname
inlets:
  1st: 
    list: source and destination.
    verbose <float>: set verbosity on or off.
outlets:
  1st:
    list: source and destination on success.
  2nd:
    bang: if an error occurs.

flags:
  -q: set quiet verbosity.
  -v: set loud verbosity.

draft: false
pdcategory: Misc

---

[file move] moves (renames) files
