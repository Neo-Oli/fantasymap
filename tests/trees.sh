#!/bin/bash
. "$(dirname $0)/framework.sh"
input='
a
a
a'
expected='
▆
▆
╹'
maptest "$input" "$expected"
