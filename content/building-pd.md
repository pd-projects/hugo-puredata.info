---
title: "Building Pd"

draft: false
---

# Building Pd

these are basic instructions on building Pd for many platforms. for in-depth instructions see [Pd manual chapter 6](https://msp.ucsd.edu/Pd_documentation/resources/chapter6.htm).

### All

download and extract the latest "stable" version source code from http://msp.ucsd.edu/software.html

### Linux

Install the core build requirements using your distribution's package
manager. For Debian, you can install the compiler chain, autotools, &
gettext with:

```sh
sudo apt-get install build-essential automake autoconf libtool gettext
sudo apt-get install libasound2-dev tcl tk
```

to compile run:

```sh
cd path/to/pd
./autogen.sh
./configure
make
```

Building should take a minute or two. If compilation was successful, you
can run Pd from the build directory without installing it:

```
cd bin
./pd
```

To install to your system using the configuration prefix (default
`/usr/local`):

```sh
sudo make install
```

If want to uninstall, make sure Pd is configured and then run:

```sh
sudo make uninstall`
```


### macOS

macOS is built on top of a BSD system and the bash commandline can be
accessed with the Terminal application in the `/Applications/Utility`
directory.

The clang compiler and associated tools are provided by Apple. If you
are running macOS 10.9+, you *do not* need to install the full Xcode
application and can install the Commandline Tools Package only by
running the following:

`xcode-select --install`

Tcl/Tk is already included macOS.

To install the autotools, gettext, and libraries for additional
features, you can use one of the open source package managers for macOS:

-   homebrew: [https://brew.sh](https://brew.sh)
    (recommended)
-   macports:
    [https://www.macports.org](https://www.macports.org)

Follow the package manager set up instructions and then install the
software you need. For example, to install the autotools & gettext using
Homebrew:

```sh
brew install automake autoconf libtool pkg-config gettext
brew link --force gettext
```

to compile run:

```sh
cd path/to/pd
./autogen.sh
./configure
make app
```

This builds Pd-#.##.#.app in the Pd source directory which can be then
be double-clicked and/or copied to `/Applications`.

### Windows

to build for Windows we use Msys2

- download the 64-bit installer from: https://www.msys2.org/

- follow installation instructions on: https://www.msys2.org/wiki/MSYS2-installation/


open the Msys2 shell and install dependencies:

```sh
pacman -S make autoconf automake libtool
pacman -S mingw64/mingw-w64-x86_64-gcc
```


install the ASIO SDK by doing the following:

- download the ASIO SDK: https://www.steinberg.net/en/company/developer.html

- uncompress asiosdk2.3.zip (or higher) into the `asio` folder of your downloaded Pd sources

- remove the version number so that you get `pure-data/asio/ASIOSDK`

open the MinGW64 shell and do

```sh
cd path/to/pd
./autogen.sh
./configure
make app
```

This will create a "pd-VERSION" directory (ie. pd-0.48.1) which can
then be used by running pd.exe in the bin directory and placed wherever
you like on your system.

