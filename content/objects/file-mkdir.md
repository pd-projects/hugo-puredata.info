---
title: file mkdir
description: create directories
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
- file which
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
    symbol: directory to be created.
    verbose <float>: set verbosity on or off.
    creationmode <octal>: restrict permissions of the to-be-created file.
outlets:
  1st:
    symbol: created directory on success.
  2nd:
    bang: when there's an error creating the directory.

flags:
  -q: set quiet verbosity.
  -v: set loud verbosity.
  -m: file creation mode (user/group/other permissions) in octal.
draft: false
pdcategory: Misc

---


This ensures that a given directory exists by creating it.

parent directories are created as needed.

it is not an error, if the requested directory already exists (and is a directory).
