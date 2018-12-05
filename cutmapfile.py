#!/usr/bin/env python3
import re, os, argparse
big=100000000000
parser = argparse.ArgumentParser()
parser.description="Best viewed when piped into `less -RS`"
parser.add_argument('file', help='Mapfile')
parser.add_argument('starty', type=int, help='Start Y', nargs="?", default=0)
parser.add_argument('startx', type=int, help='Start X', nargs="?", default=0)
parser.add_argument('endy', type=int, help='End Y', nargs="?", default=big)
parser.add_argument('endx', type=int, help='End X', nargs="?", default=big)
options = parser.parse_args()
with open (options.file, "r") as myfile:
    map=myfile.read()
if options.starty==0 and options.startx==0 and options.endx==big and options.endy==big:
    print(map)
else:
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
    print(output,end="")
