#!/usr/bin/env python3
import re, os, argparse
parser = argparse.ArgumentParser()
parser.description="Best viewed when piped into `less -RS`"
parser.add_argument('file', help='Mapfile')
parser.add_argument('starty', type=int, help='Start Y')
parser.add_argument('startx', type=int, help='Start X')
parser.add_argument('endy', type=int, help='End Y')
parser.add_argument('endx', type=int, help='End X')
options = parser.parse_args()
with open (options.file, "r") as myfile:
    map=myfile.read()
lines=map.split('\n')
iline=0
output=""
for line in lines:
    iline+=1
    if iline >= options.starty and iline <= options.endy:
        icol=0
        charsinline=list(line)
        for char in charsinline:
            icol+=1
            if icol >= options.startx and icol <= options.endx:
                output+=char
        output+='\n'
print(output)
