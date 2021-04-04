#!/bin/bash
# vim:nolist
. "$(dirname $0)/framework.sh"
input='
NNNN
NNNN
NNNN'
expected='
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="12.0px" height="11.5px" viewBox="0 0 12.0 11.5" style="letter-spacing:0em;font-size:10px;font-family:&apos;DejaVu Sans Mono&apos;;stroke:none">
    <text y="8.5" x="0.0" style="fill:#000000">██</text>
<text y="8.5" x="0.0" style="fill:#000000">NN</text>
</svg>'
maptest "$input" "$expected" "-s" "1 1 1 2"
