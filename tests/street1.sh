#!/bin/bash
. "$(dirname $0)/framework.sh"
input='
NNNN
NxNN
NxxN
NxNN
NNNN'
expected='
NNNN
N╻NN
N┣╸N
N╹NN
NNNN'
maptest "$input" "$expected"
