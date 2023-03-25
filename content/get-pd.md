---
title: "Get Pd"

draft: false
---

# Get Pd 



### Main Pd Flavours

Pure Data is an Open Source project and embraces derivatives. Notable flavours of Pd include:

### [Pd-vanilla](http://msp.ucsd.edu/software.html)

Miller S. Puckette's original distribution of Pd.

### [Pd-ceammc](https://ceammc.github.io/pd-help/)

Fully compatible with Pd Vanilla, this flavour is enhanced with some UI tweaks, including some from (the now unmaintained and deprecated) Pd-Extended (like visually differentiating control and signal in/outlets). It carries some pre-installed externals (but none from Pd-extended); most notably it has the ceammc library (that you can also install on Pd Vanilla and use in Vanilla most of what this flavour offers).

### [Pd-L2Ork](https://l2ork.music.vt.edu/main/make-your-own-l2ork/software/)

Pd-L2Ork 1.x started in 2009 as a fork of Pd-extended (but for Linux only), including the same pre-installed externals as Pd-extended and more. A cross platform version was released in 2017 named Purr Data (now an independent project, see below), which also included a port to a new HTML5 front-end GUI (instead of tcl/tk). In the fall of 2021, Pd-L2Ork provided new releases unrelated to Purr Data, but including the same HTML5 GUI port provided in Purr Data. GUI externals made for Pd-Vanilla that use tcl/tk are not compatible to the HTML5 GUI front-end, and some GUI externals from Pd-extended haven't been ported yet. Note that there are also some incompatibilities/differences between the core of Pd-Vanilla and Pd-L2Ork.

### [Purr Data](https://www.purrdata.net/)

Started as an updated version of Pd-L2Ork 1.x ported to an HTML5 GUI front-end GUI. This flavour also includes pre-installed externals from Pd-Extended and others more. It has the same caveat that GUI externals made for Pd-Vanilla are not compatible to the HTML5 GUI front-end, and some GUI externals from Pd-extended haven't been ported yet. Note that there are also some incompatibilities/differences between the core of Pd-Vanilla and Purr Data. Other than that, you must now also consider Pd-L2Ork and Purr Data incompatible to each other as well, meaning that things that work in one may not work in the other.

### [plugdata](https://plugdata.org/)

Pd with a re-imagined GUI, available both as a VST3/AU/LV2 plugin or as a standalone app. Compatible with Pd-vanilla, and comes with the ELSE and Cyclone libraries included.

