#!/bin/bash
. "$(dirname $0)/framework.sh"
input='
NNNN
NrrN
NrNN
Nx+N
N+NN
NNNN'
expected='
NNNN
N╔═N
N║NN
N┏╴N
N╵NN
NNNN'
maptest "$input" "$expected" "-b"
