import subprocess
from gc import collect
import json
import os
import shlex
from os.path import exists
import sys

traces = [
    '429.mcf-51B.champsimtrace.xz',
    '437.leslie3d-134B.champsimtrace.xz',
    '433.milc-127B.champsimtrace.xz',
    '470.lbm-1274B.champsimtrace.xz',
    'pr-10.trace.gz',
    'bc-0.trace.gz',
    'bfs-10.trace.gz',
    'cc-13.trace.gz'
]

four = [
    [traces[0], traces[1], traces[4], traces[5]],
    [traces[0], traces[1], traces[6], traces[7]],
    [traces[0], traces[1], traces[2], traces[3]],
    [traces[2], traces[3], traces[4], traces[5]],
    [traces[2], traces[3], traces[6], traces[7]],
    [traces[4], traces[5], traces[6], traces[7]],
    [traces[0], traces[2], traces[4], traces[6]],
]

two = [
    [traces[0], traces[4]],
    [traces[1], traces[5]],
    [traces[2], traces[6]],
    [traces[3], traces[7]],
    [traces[4], traces[5]],
    [traces[5], traces[6]],
    [traces[6], traces[7]],
]

one = [
    [traces[0]],
    [traces[1]],
    [traces[2]],
    [traces[3]],
    [traces[4]],
    [traces[5]],
    [traces[6]],
]

mixes = []

comm = [
    f''
]

def task1():
    # trace_list = f"traces/{trace} traces/{trace} traces/{trace} traces/{trace}"
    if len(sys.argv) < 3:
        print("workload mix [0 to 6] [1], #cores [2]missing\n")
        exit(0)
    
    print('hardcoded: #Predictor(v1/v2) [3] ')
    tag = ""
    path = ""
    V = "V2"

    ''' right now i need to check V2 only'''
    # if sys.argv[3] == "v1":
    #     V="V1"
    # else:
    #     V="V2"

    cmd1 = f"./bin/champsim_1Core{V} --warmup_instructions 0 --simulation_instructions 200000000 "
    cmd2 = f"./bin/champsim_2Core{V} --warmup_instructions 0 --simulation_instructions 200000000 "
    cmd4 = f"./bin/champsim_4Core{V} --warmup_instructions 0 --simulation_instructions 200000000 "
    
    cmd = ""

    if str(sys.argv[2]) == "one":
        mixes=one
        cmd = cmd1
    if str(sys.argv[2]) == "two":
        mixes=two
        cmd = cmd2
    if str(sys.argv[2]) == "four":
        mixes=four
        cmd = cmd4

    for trace in mixes[int(sys.argv[1])]:
        path = path + f"../traces/{trace} "
        if tag == "":
            tag = trace.split('.')[0]
        else:
            tag = tag + "-" + trace.split('.')[0]
    
    cmd = cmd + path
    try:
        print(f'traces={path}')
        print(f'Predictor V#={V}')
        print(f'0M, 200M')
        print(f"running... {cmd}")
        subprocess.run(shlex.split(cmd))
    except subprocess.CalledProcessError as e:
        print("error: ", e.output, trace)

task1()
