---
title: file which
description: locate a file
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
- file glob
- file stat
- file isfile
- file isdirectory
- file size
- file copy
- file move
- file delete
- file split
- file join
- file splitext
- file splitname
inlets:
  1st:
    symbol: file to locate using Pd's search-paths.
    verbose <float>: set verbosity on or off.
outlets:
  1st:
    list: symbol path of located file and directory flag.
  2nd:
    float: when there's an error creating the directory.

flags:
  -q: set quiet verbosity.
  -v: set loud verbosity.

draft: false
pdcategory: Misc

---


[file which] tries to locate the file in using Pd's search-paths and returns the resolved path.

notes:

- currently this only works for files, not for directories!

- currently only the first match is returned
