---
title: file mkdir
description: create directories
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
flags:
- flag: -q
  description: set quiet verbosity.
- flag: -v
  description: set loud verbosity.
- flag: -m
  description: file creation mode (user/group/other permissions) in octal.
inlets:
  1st:
    creationmode <octal>: restrict permissions of the to-be-created file.
    symbol: directory to be created.
    verbose <float>: set verbosity on or off.
outlets:
  1st:
    symbol: created directory on success.
  2nd:
    bang: when there's an error creating the directory.
draft: false
---
This ensures that a given directory exists by creating it.

parent directories are created as needed.

it is not an error, if the requested directory already exists (and is a directory).
