#!/bin/bash
. "$(dirname $0)/framework.sh"
input='
NNN
NxN
NNN'
expected='
NNN
N▪N
NNN'
maptest "$input" "$expected"
