---
title: file join
description: "'join' a list of components using '/' as the separator."
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
- file move
- file delete
- file split
- file splitext
- file splitname
inlets:
  1st: 
    list: list of components to join.
outlets:
  1st:
    symbol: joined path or file.
  2nd:
    Inactive Outlet!: 


draft: false
pdcategory: Misc

---

This objects perform common string operations on filenames. no checks are performed verifying the validity/existence of any path-component.

'file join' object accepts both symbols and numbers.




