#!/usr/bin/env python3
import re, sys, argparse
parser = argparse.ArgumentParser()
parser.description="Best viewed when piped into `less -RS`"
parser.add_argument('file', help='Mapfile')
parser.add_argument('-x', action='store_true', help='print HTML instead of ANSI')
parser.add_argument('-d', action='store_true', help='Doesn\'t print html skeleton')
parser.add_argument('-v', action='store_true', help='Do not print anything. Usefull for checking for errors in the mapfile')
options = parser.parse_args()


with open (options.file, "r") as myfile:
    map=myfile.read()



objects={}
objects['w']={}
objects['w']['name']="water"
objects['w']['r']="▓"
objects['w']['color']="blue"
objects['w']['bgcolor']="on_white"

objects[',']={}
objects[',']['name']="sand"
objects[',']['r']="▓"
objects[',']['color']="yellow"
objects[',']['bgcolor']="on_white"

objects['.']={}
objects['.']['name']="grass"
objects['.']['r']="░"
objects['.']['color']="green"
objects['.']['bgcolor']="on_white"

objects['i']={}
objects['i']['name']="snow"
objects['i']['r']="▓"
objects['i']['color']="iwhite"
objects['i']['bgcolor']="on_white"

objects['s']={}
objects['s']['name']="street"
objects['s']['r']="█"
objects['s']['color']="iwhite"
objects['s']['bgcolor']="on_white"


objects['y']={}
objects['y']['name']="farmland"
objects['y']['r']="░"
objects['y']['color']="yellow"
objects['y']['bgcolor']="on_black"
objects['y']['xggpmcolor']="#AA9106"

objects['a']={}
objects['a']['name']="forrest"
objects['a']['r']="♣"
objects['a']['color']="igreen"
objects['a']['bgcolor']="on_white"

objects['ä']={}
objects['ä']['name']="forrest2"
objects['ä']['r']="♠"
objects['ä']['color']="igreen"
objects['ä']['bgcolor']="on_white"

objects['à']={}
objects['à']['name']="palmforrest"
objects['à']['r']="Γ"
objects['à']['color']="igreen"
objects['à']['bgcolor']="on_white"

objects['b']={}
objects['b']['name']="building"
objects['b']['r']="▪"
objects['b']['color']="iblack"
objects['b']['bgcolor']="on_white"

objects['B']={}
objects['B']['name']="multiblock_building"
objects['B']['r']="█"
objects['B']['color']="iblack"
objects['B']['bgcolor']="on_white"

objects['L']={}
objects['L']['name']="special_building_lighthouse"
objects['L']['r']="◘"
objects['L']['color']="ired"
objects['L']['bgcolor']="on_white"


objects['m']={}
objects['m']['name']="mountain"
objects['m']['r']="▲"
objects['m']['color']="iblack"
objects['m']['bgcolor']="on_white"

objects['0']={}
objects['0']['name']="street_crossing"
objects['0']['r']="┼"
objects['0']['color']="iblack"
objects['0']['bgcolor']="on_white"

objects['-']={}
objects['-']['name']="street_h"
objects['-']['r']="─"
objects['-']['color']="iblack"
objects['-']['bgcolor']="on_white"

objects['|']={}
objects['|']['name']="street_v"
objects['|']['r']="│"
objects['|']['color']="iblack"
objects['|']['bgcolor']="on_white"

objects['1']={}
objects['1']['name']="street_c1"
objects['1']['r']="┐"
objects['1']['color']="iblack"
objects['1']['bgcolor']="on_white"

objects['2']={}
objects['2']['name']="street_c2"
objects['2']['r']="┌"
objects['2']['color']="iblack"
objects['2']['bgcolor']="on_white"

objects['3']={}
objects['3']['name']="street_c3"
objects['3']['r']="┘"
objects['3']['color']="iblack"
objects['3']['bgcolor']="on_white"

objects['4']={}
objects['4']['name']="street_c4"
objects['4']['r']="└"
objects['4']['color']="iblack"
objects['4']['bgcolor']="on_white"

objects['5']={}
objects['5']['name']="street_c5"
objects['5']['r']="┬"
objects['5']['color']="iblack"
objects['5']['bgcolor']="on_white"

objects['6']={}
objects['6']['name']="street_c6"
objects['6']['r']="┴"
objects['6']['color']="iblack"
objects['6']['bgcolor']="on_white"

objects['7']={}
objects['7']['name']="street_c7"
objects['7']['r']="┤"
objects['7']['color']="iblack"
objects['7']['bgcolor']="on_white"

objects['8']={}
objects['8']['name']="street_c8"
objects['8']['r']="├"
objects['8']['color']="iblack"
objects['8']['bgcolor']="on_white"

objects['9']={}
objects['9']['name']="street_none"
objects['9']['r']="▪"
objects['9']['color']="iwhit"
objects['9']['bgcolor']="on_white"




objects['0r']={}
objects['0r']['name']="rails_crossing"
objects['0r']['r']="╬"
objects['0r']['color']="ired"
objects['0r']['bgcolor']="on_white"

objects['-r']={}
objects['-r']['name']="rails_h"
objects['-r']['r']="═"
objects['-r']['color']="ired"
objects['-r']['bgcolor']="on_white"

objects['|r']={}
objects['|r']['name']="rails_v"
objects['|r']['r']="║"
objects['|r']['color']="ired"
objects['|r']['bgcolor']="on_white"

objects['1r']={}
objects['1r']['name']="rails_c1"
objects['1r']['r']="╗"
objects['1r']['color']="ired"
objects['1r']['bgcolor']="on_white"

objects['2r']={}
objects['2r']['name']="rails_c2"
objects['2r']['r']="╔"
objects['2r']['color']="ired"
objects['2r']['bgcolor']="on_white"

objects['3r']={}
objects['3r']['name']="rails_c3"
objects['3r']['r']="╝"
objects['3r']['color']="ired"
objects['3r']['bgcolor']="on_white"

objects['4r']={}
objects['4r']['name']="rails_c4"
objects['4r']['r']="╚"
objects['4r']['color']="ired"
objects['4r']['bgcolor']="on_white"

objects['5r']={}
objects['5r']['name']="rails_c5"
objects['5r']['r']="╦"
objects['5r']['color']="ired"
objects['5r']['bgcolor']="on_white"

objects['6r']={}
objects['6r']['name']="rails_c6"
objects['6r']['r']="╩"
objects['6r']['color']="ired"
objects['6r']['bgcolor']="on_white"

objects['7r']={}
objects['7r']['name']="rails_c7"
objects['7r']['r']="╣"
objects['7r']['color']="ired"
objects['7r']['bgcolor']="on_white"

objects['8r']={}
objects['8r']['name']="rails_c8"
objects['8r']['r']="╠"
objects['8r']['color']="ired"
objects['8r']['bgcolor']="on_white"

objects['9r']={}
objects['9r']['name']="rails_none"
objects['9r']['r']="▪"
objects['9r']['color']="ired"
objects['9r']['bgcolor']="on_white"


objects['[']={}
objects['[']['name']="street-rails-crossing-horizontal"
objects['[']['r']="╫"
objects['[']['color']="ired"
objects['[']['bgcolor']="on_white"


objects[']']={}
objects[']']['name']="street-rails-crossing-vertical"
objects[']']['r']="╪"
objects[']']['color']="ired"
objects[']']['bgcolor']="on_white"

objects['j']={}
objects['j']['name']="bridgev"
objects['j']['r']="║"
objects['j']['color']="iblack"
objects['j']['bgcolor']="on_blue"

objects['q']={}
objects['q']['name']="bridgeh"
objects['q']['r']="═"
objects['q']['color']="iblack"
objects['q']['bgcolor']="on_blue"

objects['p']={}
objects['p']['name']="pool"
objects['p']['r']="▐"
objects['p']['color']="blue"
objects['p']['bgcolor']="on_white"

objects['o']={}
objects['o']['name']="pond"
objects['o']['r']="●"
objects['o']['color']="blue"
objects['o']['bgcolor']="on_white"

objects[' ']={}
objects[' ']['name']="empty"
objects[' ']['r']=" "
objects[' ']['color']="empty"
objects[' ']['bgcolor']="on_white"



empty="";reset='\033[0m';

black='\033[0;30m';
red='\033[0;31m';
green='\033[0;32m';
yellow='\033[0;33m';
blue='\033[0;34m';
purple='\033[0;35m';
cyan='\033[0;36m';
white='\033[0;37m';

on_black='\033[40m';
on_red='\033[41m';
on_green='\033[42m';
on_yellow='\033[43m';
on_blue='\033[44m';
on_purple='\033[45m';
on_cyan='\033[46m';
on_white='\033[47m';

iblack='\033[0;90m';
ired='\033[0;91m';
igreen='\033[0;92m';
iyellow='\033[0;93m';
iblue='\033[0;94m';
ipurple='\033[0;95m';
icyan='\033[0;96m';
iwhite='\033[0;97m';

on_biblack='\033[1;100m';
on_bired='\033[1;101m';
on_bigreen='\033[1;102m';
on_biyellow='\033[1;103m';
on_biblue='\033[1;104m';
on_bipurple='\033[1;105m';
on_bicyan='\033[1;106m';
on_biwhite='\033[1;107m';
if options.d:
    htmlstart="""
<div class="map"><div class="on_black">
"""
    htmlend="</div></div>"
else:
    htmlstart="""
<!DOCTYPE html><html><head><meta charset="UTF-8"><style type="text/css">
<link rel="stylesheet" href="map.css">
</style></head><body><div class="map"><div class="on_black">
"""
    htmlend="</div></div></body></html>"

output=""

lines=map.split('\n')
if options.x:
    output+=htmlstart
map=None
i=0
for line in lines:
    charsinline=list(line)
    j=0
    lastc=""
    lastfg=""
    lastbg=""
    label=False
    for c in charsinline:
        if c == ")":
            backgroundcolor="on_yellow"
            foregroundcolor="black"
            character=" "
            label=False
        elif label==True:
            backgroundcolor="on_yellow"
            foregroundcolor="black"
            character=c
        elif c == "(":
            backgroundcolor="on_yellow"
            foregroundcolor="black"
            character=" "
            label=True
        else:
            if c == "x" or c == "r":
                if c == "r":
                    rails=True
                    c="x"
                else:
                    rails=False
                try:
                    leftc=charsinline[j-1]
                except IndexError:
                    leftc=" "
                try:
                    rightc=charsinline[j+1]
                except IndexError:
                    rightc=" "
                try:
                    upc=re.findall(".", lines[i-1])[j]
                except IndexError:
                    upc=" "
                try:
                    downc=re.findall(".", lines[i+1])[j]
                except IndexError:
                    downc=" "
                if rails:
                    uptrue=upc in ["r","[", "]"]
                    downtrue=downc in ["r","[", "]"]
                    lefttrue=leftc in ["r","[", "]"]
                    righttrue=rightc in ["r","[", "]"]
                else:
                    uptrue=upc in ["x","|","0","1","2","5","7","8","j","]"]
                    downtrue=downc in ["x","|","0","3","4","6","7","8","j","]"]
                    lefttrue=leftc in ["x","-","0","2","4","5","6","8","q","["]
                    righttrue=rightc in ["x","-","0","1","3","5","6","7","q","["]
                if uptrue and downtrue and lefttrue and righttrue:
                    c="0"
                elif not uptrue and not downtrue and lefttrue and righttrue:
                    c="-"
                elif not uptrue and not downtrue and lefttrue and not righttrue:
                    c="-"
                elif not uptrue and not downtrue and not lefttrue and righttrue:
                    c="-"
                elif uptrue and downtrue and not lefttrue and not righttrue:
                    c="|"
                elif uptrue and not downtrue and not lefttrue and not righttrue:
                    c="|"
                elif not uptrue and downtrue and not lefttrue and not righttrue:
                    c="|"
                elif not uptrue and downtrue and lefttrue and not righttrue:
                    c="1"
                elif not uptrue and downtrue and not lefttrue and righttrue:
                    c="2"
                elif uptrue and not downtrue and lefttrue and not righttrue:
                    c="3"
                elif uptrue and not downtrue and not lefttrue and righttrue:
                    c="4"
                elif not uptrue and downtrue and lefttrue and righttrue:
                    c="5"
                elif uptrue and not downtrue and lefttrue and righttrue:
                    c="6"
                elif uptrue and downtrue and lefttrue and not righttrue:
                    c="7"
                elif uptrue and downtrue and not lefttrue and righttrue:
                    c="8"
                elif not uptrue and not downtrue and not lefttrue and not righttrue:
                    c="9"
                else:
                    c="9"
                if rails:
                    c+="r"
            try:
                foregroundcolor=objects[c]["color"]
            except KeyError:
                print("\nError at line:"+str(i+1)+":"+str(j+1))
                exit()
            try:
                backgroundcolor=objects[c]["bgcolor"]
            except KeyError:
                backgroundcolor="empty"
            character=objects[c]["r"]
        if options.x:
            if lastbg==backgroundcolor and lastfg==foregroundcolor:
                    output+=character
            else:
                if not j==0:
                    output+="</i>"
                output+="<i class=\""+foregroundcolor+" "+backgroundcolor+"\">"+character
            if j==len(charsinline)-1:
                    output+="</i>"
        else:
            if lastbg is not backgroundcolor or lastfg is not foregroundcolor:
                output+=globals()[foregroundcolor]+globals()[backgroundcolor]
            output+=character
        lastbg=backgroundcolor
        lastfg=foregroundcolor
        lastc=c
        lastcharacter=character
        j+=1
    if options.x:
        if not options.v:
            output+="<br />"
    else:
        output+=reset+"\n"
    i+=1
if options.x:
    if not options.v:
        output+=htmlend
if not options.v:
    print(output)
