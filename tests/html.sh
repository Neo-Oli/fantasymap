#!/bin/bash
# vim:nolist
. "$(dirname $0)/framework.sh"
input='
N'
expected='<div class="map"><i class="black on_black">N</i><br /></div>'
maptest "$input" "$expected" "-xH"
