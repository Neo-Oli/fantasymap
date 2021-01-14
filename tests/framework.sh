#!/bin/bash
cd "$(dirname $0)"
maptest(){
    input=$(echo "$1"|sed '/^$/d')
    expected=$(echo "$2"|sed '/^$/d')
    output="$(NOPROGRESS=true ../map.py -b 2>&1 <(echo "$input"))"
    if [ "$output" != "$expected" ];then
        echo "Test failed: $0"
        echo "input:"
        echo "$input"
        echo "output:"
        echo "$output"
        echo "expected:"
        echo "$expected"
        exit 1
    fi
}
