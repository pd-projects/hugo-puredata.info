---
title: garray
description: graphical array (messages received via array name).
categories:
- object
pdcategory: Arrays & Tables
last_update: '0.52'
see_also:
- inlet
- namecanvas
- array
methods:
- method: list
  description: sets values into array, fisty element is starting index (from 0).
- method: const <float>
  description: optional float sets a constant value to all indexes (default 0).
- method: resize <float>
  description: resizes the array.
- method: sinesum <list>
  description: first element sets array size, remaining elements set amplitude of
    sine components.
- method: cosinesum <list>
  description: first element sets array size, remaining elements set amplitude of
    cosine components.
- method: print
  description: prints array information (name, type, size) on the terminal window.
- method: normalize <float>
  description: normalizes to maximum absolute amplitude set by optional float (default
    1).
- method: read <symbol>
  description: load contents from a text file with the symbol name.
- method: write <symbol>
  description: save contents to a text file with the symbol name.
- method: rename <symbol>
  description: renames the array to a new name defined by the given symbol.
- method: bounds <list>
  description: sets rectangle bounds (xmin, ymax, xmax, ymin).
- method: xticks <list>
  description: sets a point to put a tick, the interval between ticks, and the number
    of ticks overall per large tick.
- method: yticks <list>
  description: same as above for the 'y' axis.
- method: xlabels <list>
  description: first element is a label offset, remaining are the values to label.
- method: ylabels <list>
  description: first element is a label offset, remaining are the values to label.
- method: vis <float>
  description: zero hides array, non zero shows it.
- method: width <float>
  description: sets array's width (default 1).
- method: color <float>
  description: sets array color in the same format as Data Structures.
- method: style <float>
  description: sets display style (0-point, 1-polygon, 2-bezier).
- method: edit <float>
  description: non zero allows editing with the mouse, zero prevents it.
draft: false
---
Input is via send names
