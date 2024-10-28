## Script Name: full_ops.py

## Usage: python3 full_ops.py c_in n_wv

## Parameters:
# c_in: input channel count
# n_wv: number of weight vectors

## Output: Outputs the channel count, height count, width count, number of additions, number of multipications, and number of divisions performed

## Written by Carl Hayden

## Importing Libraries
import math
import sys # argv

## Initialize Script Arguments
c_in = float('nan')
n_wv = float('nan')

## Parse Script Arguments
if len(sys.argv)==3:
    c_in = float(sys.argv[1])
    n_wv = float(sys.argv[2])

else:
    print(\
        'Usage: '\
        'python3 full_ops.py c_in n_wv'\
    )
    exit()

## Main Script
muls = n_wv * c_in
adds = n_wv * c_in

c_out = n_wv
h_out = w_out = 1
divs = 0

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed