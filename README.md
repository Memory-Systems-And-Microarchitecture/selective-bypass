<p align="center">
  <h1 align="center"> ChampSim </h1>
</p>

# Clone ChampSim repository
```
git clone [https://github.com/ChampSim/ChampSim.git](https://github.com/Memory-Systems-And-Microarchitecture/selective-bypass)
```

# Compile

ChampSim takes a JSON configuration script. Examine `champsim_config.json` for a fully-specified example. All options described in this file are optional and will be replaced with defaults if not specified. The configuration scrip can also be run without input, in which case an empty file is assumed.
```
$ ./config.sh {1core.json or 2core.json or champsim_config.json}
$ make -j9 TAG={uniqueid whatever you want to append to binary name or it could be just empty field}
```

# Download DPC-3 trace

Professor Daniel Jimenez at Texas A&M University kindly provided traces for the 3rd Data Prefetching Championship (DPC-3). They can be found here (http://hpca23.cse.tamu.edu/champsim-traces/speccpu). A set of traces used for the 2nd Cache Replacement Championship (CRC-2) can be found from this link. (http://bit.ly/2t2nkUj)

# Run simulation

Execute the binary directly.
```
$ bin/champsim --warmup_instructions 200000000 --simulation_instructions 500000000 ~/path/to/traces/600.perlbench_s-210B.champsimtrace.xz
```

Good luck and be a champion! <br>
