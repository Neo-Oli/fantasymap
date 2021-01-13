#!/bin/bash
. "$(dirname $0)/framework.sh"
input='
NNrNN
NxcxN
NNrNN'
expected='
NN║NN
N╺╫╸N
NN║NN'
maptest "$input" "$expected"
