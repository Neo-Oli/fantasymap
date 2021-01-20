#!/bin/bash
. "$(dirname $0)/framework.sh"
input='
NNNN
NxxN
Nx|N
NxxN
NNNN'
expected='
NNNN
N┏┓N
N┃┃N
N┗┛N
NNNN'
maptest "$input" "$expected" "-b"
