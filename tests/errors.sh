#!/bin/bash
# vim:nolist
. "$(dirname $0)/framework.sh"
input='
N½ N'
expected='
Error at line:1 char:2 c:½
Error at line:1 char:3 c: 
NEEN'
maptest "$input" "$expected" "-b"
