---
title: "Building on Windows"

draft: false
---



## Building on Windows with Msys2

Download the 64-bit installer from:

https://www.msys2.org/

Follow installation instructions on: https://www.msys2.org/wiki/MSYS2-installation/

Add with pacman these packages:

`pacman -S make autoconf automake libtool`

Then the 32-bit compiler:

`pacman -S mingw32/mingw-w64-i686-gcc`

also the 64-bit compiler:

`pacman -S mingw64/mingw-w64-x86_64-gcc`
