---
title: "List of objects"

draft: false
---



## List of objects

The following is a list of built-in objects in Pd. (Not included in this 
list are messages, atoms, graphs, etc. which aren't typed into object 
boxes but come straight off the "add" menu.) 

### General 

[[bang]](bang) - output a bang message\
[[float]](float) - store and recall a number\
[[symbol]](symbol) - store and recall a symbol\
[[int]](int) - store and recall an integer\
[[send]](send) - send a message to a named object\
[[receive]](receive) - catch "sent" messages\
[[select]](select) - test for matching numbers or symbols\
[[route]](route) - route messages according to first element\
[[pack]](pack) - make compound messages\
[[unpack]](unpack) - get elements of compound messages\
[[trigger]](trigger) - sequence and convert messages\
[[spigot]](spigot) - interruptible message connection\
[[moses]](moses) - part a numeric stream\
[[until]](until) - looping mechanism\
[[print]](print) - print out messages\
[[trace]](trace) - message tracing for debugging\
[[makefilename]](makefilename) - format a symbol with a variable field\
[[change]](change) - remove repeated numbers from a stream\
[[swap]](swap) - swap two numbers\
[[value]](value) - shared numeric value\
[[list]](list) - manipulate lists\
[[list append]](list-append)\
[[list prepend]](list-prepend)\
[[list store]](list-store)\
[[list split]](list-split)\
[[list trim]](list-trim)\
[[list length]](list-length)\
[[list fromsymbol]](list-fromsymbol)\
[[list tosymbol]](list-tosymbol)

### Time 

[[delay]](delay) - send a message after a time delay\
[[metro]](metro) - send a message periodically\
[[line]](line) - send a series of linearly stepped numbers\
[[timer]](timer) - measure time intervals\
[[cputime]](cputime) - measure CPU time\
[[realtime]](realtime) - measure real time\
[[pipe]](pipe) - dynamically growable delay line for numbers

### Math 

[[expr]](expr-family) - C-style expressions\
[[+]](plus) - arithmetic\
[[-]](minus)\
[[*]](mul)\
[[/]](divide)\
[[max]](max)\
[[min]](min)\
[[==]](eq) - relational tests\
[[!=]](neq)\
[[>]](gt)\
[[<]](lt)\
[[>=]](ge)\
[[<=]](le)\
[[&]](and) - bit twiddling\
[[&&]](andand)\
[[|]](or)\
[[||]](oror)\
[[&lt;&lt;]](lshift)\
[[&gt;&gt;]](rshift)\
[[mtof]](mtof) - convert acoustical units\
[[ftom]](ftom)\
[[powtodb]](powtodb)\
[[dbtopow]](dbtopow)\
[[rmstodb]](rmstodb)\
[[dbtorms]](dbtorms) \

----------above done --------------

[[sin]](math-functions) - higher math\
[[cos]](math-functions)\
[[tan]](math-functions)\
[[atan]](math-functions)\
[[atan2]](math-functions)\
[[sqrt]](math-functions)\
[[pow]](math-functions)\
[[log]](math-functions)\
[[exp]](math-functions)\
[[abs]]( math-functions)\
[[%]](percent)\
[[mod]](mod)\
[[div]](div)\
[[wrap]](math-functions)\
[[random]](random) - lower math\
[[clip]](clip) - force a number into a range


### I/O via MIDI, OSC, and FUDI 

[[notein]](midi-in#notein) - MIDI input\
[[ctlin]](midi-in#ctlin)\
[[pgmin]](midi-in#pgmin)\
[[bendin]](midi-in#bendin)\
[[touchin]](midi-in#touchin)\
[[midiin]](midi-in#midiin)\
[[polytouchin]](midi-in#polytouchin)\
[[sysexin]](midi-in#sysexin)\
[[midirealtimein]](midi-in#midirealtimein)\
[[noteout]](midi-out#noteout) - MIDI output\
[[ctlout]](midi-out#ctlout)\
[[pgmout]](midi-out#pgmout)\
[[bendout]](midi-out#bendout)\
[[touchout]](midi-out#touchout)\
[[polytouchout]](midi-out#polytouchout)\
[[midiout]](midi-out#midiout)\
[[makenote]](makenote) - schedule delayed "note off" message for a note-on\
[[stripnote]](stripnote) - strip "note off" messages\
[[oscparse]](osc-format-parse) - OSC messages to and from Pd lists\
[[oscformat]](osc-format-parse)\
[[fudiparse]](fudi-format-parse) - FUDI messages to and from Pd lists\
[[fudiformat]](fudi-format-parse)

### Arrays & Tables 

[[tabread]](tabread) - read a number from a table\
[[tabread4]](tabread4) - read a number from a table\
[[tabwrite]](tabwrite) - write a number to a table\
[[soundfiler]](soundfiler) - read and write tables to soundfiles\
[[table]](array) - create a named table\
[[array]](array) - general array creation and manipulation

### Misc 

[[loadbang]]( # ) - bang on load\
[[declare]]( # ) - set search path and/or load libraries\
[[savestate]]( # ) - mechanism for saving state of an abstraction\
[[pdcontrol]]( # ) - communicate with canvas (for example, to get directory)\
[[netsend]]( # ) - send messages over the internet\
[[netreceive]]( # ) - receive them\
[[qlist]]( # ) - message sequencer\
[[textfile]]( # ) - file to message converter\
[[text]]( # ) - general text handling\
[[file]]( # ) - low-level file operations\
[[openpanel]]( # ) - "Open" dialog\
[[savepanel]]( # ) - "Save as" dialog\
[[bag]]( # ) - set of numbers\
[[poly]]( # ) - polyphonic voice allocation\
[[key]]( # ) - numeric key values from keyboard\
[[keyup]]( # )\
[[keyname]]( # ) - symbolic key name

### Audio Math 

[[expr~]]( # ) - C-style expressions\
[[fexpr~]]( # )\
[[+~]]( # ) - arithmetic on audio signals\
[[-~]]( # )\
[[*~]]( # )\
[[/~]]( # )\
[[max~]]( # ) - maximum or minimum of 2 inputs\
[[min~]]( # )\
[[clip~]]( # ) - constrict signal to lie between two bounds\
[[sqrt~]]( # ) - approximate (16-bit) square root\
[[rsqrt~]]( # ) - reciprocal square root\
[[q8_sqrt~]]( # ) - fast, cheap 8 bits versions\
[[q8_rsqrt~]]( # )\
[[wrap~]]( # ) - wraparound (fractional part)\
[[fft~]]( # ) - complex forward discrete Fourier transform\
[[ifft~]]( # ) - complex inverse discrete Fourier transform\
[[rfft~]]( # ) - real forward discrete Fourier transform\
[[rifft~]]( # ) - real inverse discrete Fourier transform\
[[pow~]]( # ) - math\
[[log~]]( # )\
[[exp~]]( # )\
[[abs~]]( # )\
[[framp~]]( # ) - estimate frequency and amplitude of FFT components\
[[mtof~]]( # ) - acoustic conversions\
[[ftom~]]( # )\
[[rmstodb~]]( # )\
[[dbtorms~]]( # )

### General Audio Manipulation 

[[dac~]]( # ) - audio output\
[[adc~]]( # ) - audio input\
[[sig~]]( # ) - convert numbers to audio signals\
[[line~]]( # ) - generate audio ramps\
[[vline~]]( # ) - deluxe line~\
[[threshold~]]( # ) - detect signal thresholds\
[[snapshot~]]( # ) - sample a signal (convert it back to a number)\
[[vsnapshot~]]( # ) - deluxe snapshot~\
[[bang~]]( # ) - send a bang message after each DSP block\
[[samplerate~]]( # ) - get the sample rate\
[[send~]]( # ) - nonlocal signal connection with fanout\
[[receive~]]( # ) - get signal from send~\
[[throw~]]( # ) - add to a summing bus\
[[catch~]]( # ) - define and read a summing bus\
[[readsf~]]( # ) - soundfile playback from disk\
[[writesf~]]( # ) - record sound to disk\
[[print~]]( # ) - print out one or more "blocks"

### Audio Oscillators And Tables 

[[noise~]]( # ) - white noise generator\
[[phasor~]]( # ) - sawtooth oscillator\
[[cos~]]( # ) - cosine\
[[osc~]]( # ) - cosine oscillator\
[[tabwrite~]]( # ) - write to a table\
[[tabplay~]]( # ) - play back from a table (non-transposing)\
[[tabread~]]( # ) - non-interpolating table read\
[[tabread4~]]( # ) - four-point interpolating table read\
[[tabosc4~]]( # ) - wavetable oscillator\
[[tabsend~]]( # ) - write one block continuously to a table\
[[tabreceive~]]( # ) - read one block continuously from a table

### Audio Filters 

[[vcf~]]( # ) - voltage controlled filter\
[[env~]]( # ) - envelope follower\
[[hip~]]( # ) - high pass filter\
[[lop~]]( # ) - low pass filter\
[[slop~]]( # ) - slew-limiting (nonlinear) low pass filter\
[[bp~]]( # ) - band pass filter\
[[biquad~]]( # ) - raw filter\
[[samphold~]]( # ) - sample and hold unit\
[[print~]]( # ) - print out one or more "blocks"\
[[rpole~]]( # ) - raw real-valued one-pole filter\
[[rzero~]]( # ) - raw real-valued one-zero filter\
[[rzero_rev~]]( # ) - time-reversed\
[[cpole~]]( # ) - corresponding complex-valued filters\
[[czero~]]( # )\
[[czero_rev~]]( # )

### Audio Delay 

[[delwrite~]]( # ) - write to a delay line\
[[delread~]]( # ) - read from a delay line\
[[delread4~]]( # ) - read with a time-varying delay time\
[[vd~]]( # )

### Subwindows 

[[pd]]( # ) - define a subwindow\
[[inlet]]( # ) - add an inlet to a pd\
[[outlet]]( # ) - add an outlet to a pd\
[[inlet~]]( # ) - signal versions\
[[outlet~]]( # )\
[[clone]]( # ) - multiple copies of a patch\
[[namecanvas]]( # ) - attach a name to a pd window\
[[block~]]( # ) - specify block size and overlap, or, if invoked as "switch", also switch subpatches on and off\
[[switch]]( # )

### Data Templates 

[[struct]]( # ) - define a data structure\
[[drawcurve]]( # ) - draw a curve\
[[filledcurve]]( # )\
[[drawpolygon]]( # ) - draw a polygon\
[[filledpolygon]]( # )\
[[drawtext]]( # ) - draw text\
[[drawsymbol]]( # )\
[[plot]]( # ) - plot an array field\
[[drawnumber]]( # ) - print a numeric value

### Accessing Data 

[[pointer]]( # ) - point to an object belonging to a template\
[[get]]( # ) - get numeric fields\
[[set]]( # ) - change numeric fields\
[[element]]( # ) - get an array element\
[[getsize]]( # ) - get the size of an array\
[[setsize]]( # ) - change the size of an array\
[[append]]( # ) - add an element to a list\
[[scalar]]( # ) - create a single scalar

### "EXTRA" (patches and externs in pd/extra) 

[[sigmund~]]( # ) - pitch tracker\
[[bonk~]]( # ) - attack detector\
[[choice]]( # ) - best match of list to templates\
[[hilbert~]]( # ) - phase quadrature / frequency shifting\
[[complex-mod~]]( # )\
[[loop~]]( # ) - phasor~ with S/H on its frequency input\
[[lrshift~]]( # ) - left and right shift (useful with FFT objects)\
[[pd~]]( # ) - run another copy of Pd (for multiprocessing)\
[[stdout]]( # )\
[[rev1~]]( # ) - reverberators\
[[rev2~]]( # )\
[[rev3~]]( # )\
[[bob~]]( # ) - Moog resonant filter model

### Obsolete 

[[scope~]]( # ) (use tabwrite~ now)\
[[template]]( # ) (use struct now)

 
 
 
 
 
 > [[quote]]( # )
