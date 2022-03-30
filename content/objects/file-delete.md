---
title: file delete
description: remove files and directories.
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
- file copy
- file move
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
    symbol: file or directory to be deleted.
    verbose <float>: set verbosity on or off.
outlets:
  1st:
    symbol: the deleted path on success.
  2nd:
    bang: if an error occurs.
draft: false
---
NOTE: deleting destroys data. there is no confirmation dialog or anything of that kind.
