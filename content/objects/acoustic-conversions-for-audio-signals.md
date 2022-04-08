acoustic conversions for audio signals

|object |Description|
|:---|---:|
|[mtof~](../mtof~/index.html) |convert MIDI pitch to frequency in hertz|
|[ftom~](../ftom~/index.html) |convert frequency in hertz to MIDI pitch|
|[dbtorms~](../dbtorms~/index.html) |convert db to rms|
|[rmstodb~](../rmstodb~/index.html) |convert rms to db|
|[powtodb~](../powtodb~/index.html) |convert power to db|
|[dbtopow~](../dbtopow~/index.html) |convert db to power|

These objects convert MIDI pitch to frequency and back, and dB to and from RMS and power. They take audio signals as input and output (and work sample by sample.) Since they call library math functions, they may be much more expensive than other workaday tilde objects such as *~ and osc~, depending on your hardware and math library.

Boundary conditions are handled "reasonably". 100 db is assigned an RMS of 1, and dbtorms~ and dbtopow~ output true zero for 0 dB and less.