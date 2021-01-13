#!/bin/bash
. "$(dirname $0)/framework.sh"
input='
NNxNN
NxxxN
NNxNN'
expected='
NN╻NN
N╺╋╸N
NN╹NN'
maptest "$input" "$expected"
