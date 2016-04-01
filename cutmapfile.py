import re, os, argparse
parser = argparse.ArgumentParser()
parser.description="Best viewed when piped into `less -RS`"
parser.add_argument('file', help='Mapfile')
parser.add_argument('line', type=int, help='Line')
parser.add_argument('lines', type=int, help='Number of lines')
parser.add_argument('col', type=int, help='Columns')
parser.add_argument('cols', type=int, help='Number of columns')
options = parser.parse_args()
with open (options.file, "r") as myfile:
    map=myfile.read()
lines=map.split('\n')
iline=0
output=""
for line in lines:
    iline+=1
    if iline >= options.line and iline <= options.line+options.lines:
        icol=0
        charsinline=list(line)
        for char in charsinline:
            icol+=1
            if icol >= options.col and icol <= options.col+options.cols:
                output+=char
        output+='\n'
print(output)
