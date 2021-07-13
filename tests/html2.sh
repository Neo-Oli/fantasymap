#!/bin/bash
# vim:nolist
. "$(dirname $0)/framework.sh"
input='
NNNN
NNNN
NNNN'
expected='<div class="map"><i class="black on_black">NN</i><br></div>'
maptest "$input" "$expected" "-xH" "1 1 1 2"
