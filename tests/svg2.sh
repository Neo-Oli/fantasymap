#!/bin/bash
# vim:nolist
. "$(dirname $0)/framework.sh"
input='
NNNN
NNNN
NNNN'
expected='
<text y="8.5" x="0.0" style="fill:#000000">██</text>
<text y="8.5" x="0.0" style="fill:#000000">NN</text>'
maptest "$input" "$expected" "-sH" "1 1 1 2"
