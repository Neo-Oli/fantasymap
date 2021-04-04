#!/bin/bash
# vim:nolist
. "$(dirname $0)/framework.sh"
input='
N'
expected='
<text y="8.5" x="0.0" style="fill:#000000">█</text>
<text y="8.5" x="0.0" style="fill:#000000">N</text>'
maptest "$input" "$expected" "-sH"
