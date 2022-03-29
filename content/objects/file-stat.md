---
title: file stat
description: get metainformation about a file/directory
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
    symbol: file or directory name.
    verbose <float>: set verbosity on or off.
outlets:
  1st:
    anything: several messages for metainformation.
  2nd:
    bang: if an error occurs.

flags:
  -q: set quiet verbosity.
  -v: set loud verbosity.

draft: false
pdcategory: Misc

---

[file stat] queries the filesystem about the given path, and outputs the collected data as a number of routable messages.
