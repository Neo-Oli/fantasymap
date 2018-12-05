#!/usr/bin/env python3


objects={}
objects['w']={}
objects['w']['name']="water"
objects['w']['r']="≈"
objects['w']['color']="white"
objects['w']['bgcolor']="on_blue"
objects['w']['bgcolor_average_overwrite']="on_yellow"

objects[',']={}
objects[',']['name']="sand"
objects[',']['r']="░"
objects[',']['color']="white"
objects[',']['bgcolor']="on_yellow"

objects['.']={}
objects['.']['name']="grass"
objects['.']['r']=""
objects['.']['r']="`"
objects['.']['color']="igreen"
objects['.']['bgcolor']="on_green"

objects['i']={}
objects['i']['name']="snow"
objects['i']['r']="▓"
objects['i']['color']="white"
objects['i']['bgcolor']="on_white"
objects['i']['bgcolor_average_overwrite']="on_white"

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
objects['a']['name']="forrest on grass"
objects['a']['r']="φ"
objects['a']['color']="igreen"
objects['a']['bgcolor']="on_green"

objects['ä']={}
objects['ä']['name']="forrest on asphalt"
objects['ä']['r']="φ"
objects['ä']['color']="igreen"
objects['ä']['bgcolor']="on_white"

objects['â']={}
objects['â']['name']="forrest on sand"
objects['â']['r']="φ"
objects['â']['color']="igreen"
objects['â']['bgcolor']="on_yellow"

objects['u']={}
objects['u']['name']="palmforrest on sand"
objects['u']['r']="Γ"
objects['u']['color']="igreen"
objects['u']['bgcolor']="on_yellow"

objects['ü']={}
objects['ü']['name']="palmforrest on asphalt"
objects['ü']['r']="Γ"
objects['ü']['color']="igreen"
objects['ü']['bgcolor']="on_white"

objects['ú']={}
objects['ú']['name']="palmforrest on grass"
objects['ú']['r']="Γ"
objects['ú']['color']="igreen"
objects['ú']['bgcolor']="on_green"

objects['b']={}
objects['b']['name']="building"
objects['b']['r']="▪"
# objects['b']['r']="⌂"
objects['b']['color']="iblack"
objects['b']['bgcolor']="on_white"

objects['B']={}
objects['B']['name']="multiblock_building"
objects['B']['r']="█"
objects['B']['color']="iblack"
objects['B']['bgcolor']="on_white"

objects['L']={}
objects['L']['name']="lighthouse"
objects['L']['r']="◘"
objects['L']['color']="ired"
objects['L']['bgcolor']="on_white"

objects['g']={}
objects['g']['name']="gravestones"
objects['g']['r']="⌂"
objects['g']['color']="iblack"
objects['g']['bgcolor']="on_green"

objects['m']={}
objects['m']['name']="mountain"
objects['m']['r']="▲"
objects['m']['color']="iblack"
objects['m']['bgcolor']="s_average"
objects['m']['bgcolor_fallback']="on_white"

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
objects['1']['name']="street_1"
objects['1']['r']="┐"
objects['1']['color']="iblack"
objects['1']['bgcolor']="on_white"

objects['2']={}
objects['2']['name']="street_2"
objects['2']['r']="┌"
objects['2']['color']="iblack"
objects['2']['bgcolor']="on_white"

objects['3']={}
objects['3']['name']="street_3"
objects['3']['r']="┘"
objects['3']['color']="iblack"
objects['3']['bgcolor']="on_white"

objects['4']={}
objects['4']['name']="street_4"
objects['4']['r']="└"
objects['4']['color']="iblack"
objects['4']['bgcolor']="on_white"

objects['5']={}
objects['5']['name']="street_5"
objects['5']['r']="┬"
objects['5']['color']="iblack"
objects['5']['bgcolor']="on_white"

objects['6']={}
objects['6']['name']="street_6"
objects['6']['r']="┴"
objects['6']['color']="iblack"
objects['6']['bgcolor']="on_white"

objects['7']={}
objects['7']['name']="street_7"
objects['7']['r']="┤"
objects['7']['color']="iblack"
objects['7']['bgcolor']="on_white"

objects['8']={}
objects['8']['name']="street_8"
objects['8']['r']="├"
objects['8']['color']="iblack"
objects['8']['bgcolor']="on_white"

objects['9']={}
objects['9']['name']="street_none"
objects['9']['r']="▪"
objects['9']['color']="iwhite"
objects['9']['bgcolor']="on_white"


objects['₀']={}
objects['₀']['name']="dirt_crossing"
objects['₀']['r']="┼"
objects['₀']['color']="iyellow"
objects['₀']['bgcolor']="s_average"
objects['₀']['bgcolor_fallback']="on_white"

objects['~']={}
objects['~']['name']="dirt_h"
objects['~']['r']="─"
objects['~']['color']="iyellow"
objects['~']['bgcolor']="s_average"
objects['~']['bgcolor_fallback']="on_white"

objects['!']={}
objects['!']['name']="dirt_v"
objects['!']['r']="│"
objects['!']['color']="iyellow"
objects['!']['bgcolor']="s_average"
objects['!']['bgcolor_fallback']="on_white"

objects['₁']={}
objects['₁']['name']="dirt_1"
objects['₁']['r']="┐"
objects['₁']['color']="iyellow"
objects['₁']['bgcolor']="s_average"
objects['₁']['bgcolor_fallback']="on_white"

objects['₂']={}
objects['₂']['name']="dirt_2"
objects['₂']['r']="┌"
objects['₂']['color']="iyellow"
objects['₂']['bgcolor']="s_average"
objects['₂']['bgcolor_fallback']="on_white"

objects['₃']={}
objects['₃']['name']="dirt_3"
objects['₃']['r']="┘"
objects['₃']['color']="iyellow"
objects['₃']['bgcolor']="s_average"
objects['₃']['bgcolor_fallback']="on_white"

objects['₄']={}
objects['₄']['name']="dirt_4"
objects['₄']['r']="└"
objects['₄']['color']="iyellow"
objects['₄']['bgcolor']="s_average"
objects['₄']['bgcolor_fallback']="on_white"

objects['₅']={}
objects['₅']['name']="dirt_5"
objects['₅']['r']="┬"
objects['₅']['color']="iyellow"
objects['₅']['bgcolor']="s_average"
objects['₅']['bgcolor_fallback']="on_white"

objects['₆']={}
objects['₆']['name']="dirt_6"
objects['₆']['r']="┴"
objects['₆']['color']="iyellow"
objects['₆']['bgcolor']="s_average"
objects['₆']['bgcolor_fallback']="on_white"

objects['₇']={}
objects['₇']['name']="dirt_7"
objects['₇']['r']="┤"
objects['₇']['color']="iyellow"
objects['₇']['bgcolor']="s_average"
objects['₇']['bgcolor_fallback']="on_white"

objects['₈']={}
objects['₈']['name']="dirt_8"
objects['₈']['r']="├"
objects['₈']['color']="iyellow"
objects['₈']['bgcolor']="s_average"
objects['₈']['bgcolor_fallback']="on_white"

objects['₉']={}
objects['₉']['name']="dirt_none"
objects['₉']['r']="▪"
objects['₉']['color']="iyellow"
objects['₉']['bgcolor']="s_average"
objects['₉']['bgcolor_fallback']="on_white"




objects['⁰']={}
objects['⁰']['name']="rails_crossing"
objects['⁰']['r']="╬"
objects['⁰']['color']="ired"
objects['⁰']['bgcolor']="on_white"

objects['=']={}
objects['=']['name']="rails_h"
objects['=']['r']="═"
objects['=']['color']="ired"
objects['=']['bgcolor']="on_white"

objects['§']={}
objects['§']['name']="rails_v"
objects['§']['r']="║"
objects['§']['color']="ired"
objects['§']['bgcolor']="on_white"

objects['¹']={}
objects['¹']['name']="rails_1"
objects['¹']['r']="╗"
objects['¹']['color']="ired"
objects['¹']['bgcolor']="on_white"

objects['²']={}
objects['²']['name']="rails_2"
objects['²']['r']="╔"
objects['²']['color']="ired"
objects['²']['bgcolor']="on_white"

objects['³']={}
objects['³']['name']="rails_3"
objects['³']['r']="╝"
objects['³']['color']="ired"
objects['³']['bgcolor']="on_white"

objects['⁴']={}
objects['⁴']['name']="rails_4"
objects['⁴']['r']="╚"
objects['⁴']['color']="ired"
objects['⁴']['bgcolor']="on_white"

objects['⁵']={}
objects['⁵']['name']="rails_5"
objects['⁵']['r']="╦"
objects['⁵']['color']="ired"
objects['⁵']['bgcolor']="on_white"

objects['⁶']={}
objects['⁶']['name']="rails_6"
objects['⁶']['r']="╩"
objects['⁶']['color']="ired"
objects['⁶']['bgcolor']="on_white"

objects['⁷']={}
objects['⁷']['name']="rails_7"
objects['⁷']['r']="╣"
objects['⁷']['color']="ired"
objects['⁷']['bgcolor']="on_white"

objects['⁸']={}
objects['⁸']['name']="rails_8"
objects['⁸']['r']="╠"
objects['⁸']['color']="ired"
objects['⁸']['bgcolor']="on_white"

objects['⁹']={}
objects['⁹']['name']="rails_none"
objects['⁹']['r']="▪"
objects['⁹']['color']="ired"
objects['⁹']['bgcolor']="on_white"


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
objects['p']['name']="pool_right"
objects['p']['r']="▐"
objects['p']['color']="blue"
objects['p']['bgcolor']="on_white"

objects['P']={}
objects['P']['name']="pool_left"
objects['P']['r']="▌"
objects['P']['color']="blue"
objects['P']['bgcolor']="on_white"

objects['o']={}
objects['o']['name']="pond"
objects['o']['r']="●"
objects['o']['color']="blue"
objects['o']['bgcolor']="on_white"

objects['t']={}
objects['t']['name']="Animal"
objects['t']['r']="."
objects['t']['color']="iblack"
objects['t']['bgcolor']="s_average"
objects['t']['bgcolor_fallback']="on_green"

objects[' ']={}
objects[' ']['name']="empty"
objects[' ']['r']=" "
objects[' ']['color']="black"
objects[' ']['bgcolor']="on_white"

objects['(']={}
objects['(']['name']="label_start"
objects['(']['r']="("
objects['(']['color']="black"
objects['(']['bgcolor']="on_yellow"

objects[')']={}
objects[')']['name']="empty"
objects[')']['r']=" "
objects[')']['color']=objects['(']['color']
objects[')']['bgcolor']=objects['(']['bgcolor']

reset='\033[0m'

black='\033[0;30m';vimblack=0
red='\033[0;31m';vimred=1
green='\033[0;32m';vimgreen=2
yellow='\033[0;33m';vimyellow=3
blue='\033[0;34m';vimblue=4
purple='\033[0;35m';vimpurple=5
cyan='\033[0;36m';vimcyan=6
white='\033[0;37m';vimwhite=7

on_black='\033[40m';vimon_black=vimblack
on_red='\033[41m';vimon_red=vimred
on_green='\033[42m';vimon_green=vimgreen
on_yellow='\033[43m';vimon_yellow=vimyellow
on_blue='\033[44m';vimon_blue=vimblue
on_purple='\033[45m';vimon_purple=vimpurple
on_cyan='\033[46m';vimon_cyan=vimcyan
on_white='\033[47m';vimon_white=vimwhite

iblack='\033[0;90m';vimiblack=8
ired='\033[0;91m';vimired=9
igreen='\033[0;92m';vimigreen=10
iyellow='\033[0;93m';vimiyellow=11
iblue='\033[0;94m';vimiblue=12
ipurple='\033[0;95m';vimipurple=13
icyan='\033[0;96m';vimicyan=14
iwhite='\033[0;97m';vimiwhite=15

hexcolors={}
hexcolors["black"]="#000000"
hexcolors["red"]="#d81765"
hexcolors["green"]="#97D01A"
hexcolors["yellow"]="#ffbc00"
hexcolors["blue"]="#16b1fb"
hexcolors["purple"]="#ff2491"
hexcolors["cyan"]="#0fdcb6"
hexcolors["white"]="#cccccc"
hexcolors["on_black"]="#000000"
hexcolors["on_red"]="#D81765"
hexcolors["on_green"]="#97D01A"
hexcolors["on_yellow"]="#FFA800"
hexcolors["on_blue"]="#16B1FB"
hexcolors["on_purple"]="#ff2491"
hexcolors["on_cyan"]="#0fdcb6"
hexcolors["on_white"]="#cccccc"
hexcolors["iblack"]="#38252C"
hexcolors["ired"]="#FF0000"
hexcolors["igreen"]="#00bb00"
hexcolors["iyellow"]="#E1A126"
hexcolors["iblue"]="#1267b9"
hexcolors["ipurple"]="#b85ed6"
hexcolors["icyan"]="#2ddbdb"
hexcolors["iwhite"]="#ffffff"
hexcolors["on_biblack"]="#38252c"
hexcolors["on_bired"]="#FF0000"
hexcolors["on_bigreen"]="#00bb00"
hexcolors["on_biyellow"]="#E1A126"
hexcolors["on_biblue"]="#1267b9"
hexcolors["on_bipurple"]="#b85ed6"
hexcolors["on_bicyan"]="#2ddbdb"
hexcolors["on_biwhite"]="#ffffff"

# on_biblack='\033[1;100m';
# on_bired='\033[1;101m';
# on_bigreen='\033[1;102m';
# on_biyellow='\033[1;103m';
# on_biblue='\033[1;104m';
# on_bipurple='\033[1;105m';
# on_bicyan='\033[1;106m';
# on_biwhite='\033[1;107m';

import os
import re
import sys
import argparse
from uuid import uuid4

def findObject(name):
    for c in objects:
        if objects[c]["name"]==name:
            return c
    print("Error: Object not found with name: {}".format(name),file=sys.stderr)


big=100000000000
parser = argparse.ArgumentParser()
parser.description="Best viewed when piped into `less -RS`"
parser.add_argument('file', help='Mapfile')
parser.add_argument('-x', action='store_true', help='print HTML instead of ANSI')
parser.add_argument('-d', action='store_true', help='Doesn\'t print html skeleton')
parser.add_argument('-v', action='store_true', help='Do not print anything. Usefull for checking for errors in the mapfile')
parser.add_argument('-b', action='store_true', help='Don\'t print color')
parser.add_argument('-V', action='store_true', help='Print vim ftplugin file')
parser.add_argument('-i', action='store_true', help='Create png image')
parser.add_argument('-s', action='store_true', help='Create svg image')


parser.add_argument('starty', type=int, help='Start Y', nargs="?", default=0)
parser.add_argument('startx', type=int, help='Start X', nargs="?", default=0)
parser.add_argument('endy', type=int, help='End Y', nargs="?", default=big)
parser.add_argument('endx', type=int, help='End X', nargs="?", default=big)
parser.add_argument('-S', type=int, help='font size for several rendering methods', nargs="?", default=10)

options = parser.parse_args()

scale=options.S

with open (options.file, "r") as myfile:
    map=myfile.read()

block="█"
build=uuid4()
output=""
lines=map.split('\n')
del lines[-1] # delete last, empty line

if options.V:
    output="setlocal nowrap\n"
    output="{}setlocal redrawtime=10000".format(output)
    i=0
    for c in objects:
        rule="rule_{}".format(i)
        match="syn match {} /[{}]/".format(rule,c)
        try:
            fg=globals()["vim{}".format(objects[c]["color"])]
            bg=globals()["vim{}".format(objects[c]["bgcolor"])]
        except KeyError:
            fg="None"
            bg="None"
        hi="hi def {} ctermfg={} ctermbg={}".format(rule,fg,bg)
        output="{}\n{}\n{}".format(output,match,hi);
        i+=1
    print(output)
    sys.exit(0)

if options.x:
    with open ("map.css", "r") as myfile:
        css=myfile.read()
    csscolors=""
    for key in hexcolors:
        prefix=""
        if "on_" in key:
            prefix="background-"
        color=".map .{}{{{}color:{};}}".format(key,prefix,hexcolors[key])
        csscolors="{}{}".format(csscolors,color)
    htmlstart="""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
    <style>
    {}
    {}
    </style>
    </head>
    <body>""".format(css,csscolors)
    htmlend="""
    </body>
</html>"""
    if options.d:
        htmlstart=""
        htmlend=""

    htmlstart="""{}
        <div class="map">""".format(htmlstart)
    htmlend="""
        </div>
        {}""".format(htmlend)
    output+=htmlstart









elif options.s:
    wshift=0.6
    hshift=1.15
    movedown=-0.3*scale
    moveright=0*scale
    height=len(lines)*(scale*hshift)
    line=lines[0].split("#")[0]
    width=len(line)*(scale*wshift)

    outputbg=""
    outputfg=""
    svgstart="""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}px" height="{}px" viewBox="0 0 {} {}" style="letter-spacing:0em;font-size:{}px;font-family:&apos;DejaVu Sans Mono&apos;;stroke:none">
""".format(width,height,width,height,scale)
    svgend="""</svg>"""

    if options.d:
        htmlstart=""
        htmlend=""
    svglineend="</text>\n"
    output+=svgstart



elif options.i:
    wshift=0.6
    hshift=1.2

    height=round((1*scale*hshift)-1)
    line=lines[0].split("#")[0][options.startx:options.endx]
    width=round(len(line)*scale*wshift)
    imbase=[
            "#!/usr/bin/env magick-script",
            "-monitor",
            "-size {}x{}".format(width,height),
            "xc:black",
            "-font DejaVu-Sans-mono",
            "-pointsize {}".format(scale),
            "-gravity NorthWest"
            ]
    im={}

map=None
i=-1
for line in lines:
    i+=1
    if i<options.starty:
        continue
    if i>options.endy:
        continue
    if line=="":
        continue
    if options.i:
        im[i]=imbase[:]
    charsinline=list(line)
    linewidth=min([len(charsinline),options.endx])
    j=-1
    lastc=""
    lastfg=""
    lastbg=""
    for c in charsinline:
        j+=1
        if j<options.startx:
            continue
        if j>options.endx:
            continue


        if c=="#":
            #close all i tags
            if j>options.startx:
                if options.x:
                    output+="</i>"
                if options.s:
                    outputfg+=svglineend
                    outputbg+=svglineend
            break;


        # get the surounding characters

        try:
            leftc=charsinline[j-1]
        except IndexError:
            leftc=" "
        try:
            rightc=charsinline[j+1]
        except IndexError:
            rightc=" "
        try:
            upc=lines[i-1][j:j+1]
        except IndexError:
            upc=" "
        try:
            downc=lines[i+1][j:j+1]
        except IndexError:
            downc=" "
        try:
            upleftc=lines[i-1][j-1:j]
        except IndexError:
            upleftc=" "
        try:
            uprightc=lines[i-1][j+1:j+2]
        except IndexError:
            uprightc=" "

        try:
            downleftc=lines[i+1][j-1:j]
        except IndexError:
            downleftc=" "
        try:
            downrightc=lines[i+1][j+1:j+2]
        except IndexError:
            downrightc=" "


        if charsinline[0:j].count("(")>charsinline[0:j].count(")"):
            foregroundcolor=objects['(']['color']
            backgroundcolor=objects['(']['bgcolor']
            character=c
        else:
            if c in list("x+r"):
                rails=False
                dirt=False
                if c == "r":
                    rails=True
                    prefix="rails_{}"
                elif c=="+":
                    dirt=True
                    prefix="dirt_{}"
                else:
                    prefix="street_{}"
                if rails:
                    uptrue=upc in list("§r[⁰¹²⁵⁷⁸")
                    downtrue=downc in list("§r[⁰³⁴⁶⁷⁸")
                    lefttrue=leftc in list("=r]⁰²⁴⁵⁶⁸")
                    righttrue=rightc in list("=r]⁰¹³⁵⁶⁷")
                else:
                    uptrue=upc in list("x+|!012578j]⁰¹²⁵⁷⁸")
                    downtrue=downc in list("x+!|034678j]⁰³⁴⁶⁷⁸")
                    lefttrue=leftc in list("x+~-024568q[⁰²⁴⁵⁶⁸")
                    righttrue=rightc in list("x+~-013567q[⁰¹³⁵⁶⁷")
                if uptrue and downtrue and lefttrue and righttrue:
                    p="crossing"
                elif not uptrue and not downtrue and lefttrue and righttrue:
                    p="h"
                elif not uptrue and not downtrue and lefttrue and not righttrue:
                    p="h"
                elif not uptrue and not downtrue and not lefttrue and righttrue:
                    p="h"
                elif uptrue and downtrue and not lefttrue and not righttrue:
                    p="v"
                elif uptrue and not downtrue and not lefttrue and not righttrue:
                    p="v"
                elif not uptrue and downtrue and not lefttrue and not righttrue:
                    p="v"
                elif not uptrue and downtrue and lefttrue and not righttrue:
                    p="1"
                elif not uptrue and downtrue and not lefttrue and righttrue:
                    p="2"
                elif uptrue and not downtrue and lefttrue and not righttrue:
                    p="3"
                elif uptrue and not downtrue and not lefttrue and righttrue:
                    p="4"
                elif not uptrue and downtrue and lefttrue and righttrue:
                    p="5"
                elif uptrue and not downtrue and lefttrue and righttrue:
                    p="6"
                elif uptrue and downtrue and lefttrue and not righttrue:
                    p="7"
                elif uptrue and downtrue and not lefttrue and righttrue:
                    p="8"
                elif not uptrue and not downtrue and not lefttrue and not righttrue:
                    p="none"
                else:
                    p="none"
                c=findObject(prefix.format(p))
            try:
                foregroundcolor=objects[c]["color"]
            except KeyError:
                print("\nError at line:{}:{} c={}".format(str(i+1),str(j+1),c),file=sys.stderr)
                sys.exit(1)
            backgroundcolor=objects[c]["bgcolor"]
            character=objects[c]["r"]
        if backgroundcolor=="s_average":
            allcolors=[]
            for f in [upc,downc,leftc,rightc,upleftc,uprightc,downleftc,downrightc]:
                try:
                    avcolor=objects[f]["bgcolor"]
                    if "bgcolor_average_overwrite" in objects[f]:
                        avcolor=objects[f]["bgcolor_average_overwrite"]
                    elif "bgcolor_fallback" in objects[f]:
                        avcolor=objects[f]["bgcolor_fallback"]
                    allcolors.append(avcolor)
                except KeyError:
                    pass
            if allcolors:
                backgroundcolor=max(set(allcolors), key=allcolors.count)
            if backgroundcolor=="s_average":
                if "bgcolor_fallback" in objects[c]:
                    backgroundcolor=objects[c]["bgcolor_fallback"]
                else:
                    print("\nError at line:{}:{} c={}: Coulnd't determine background color".format(str(i+1),str(j+1),c),file=sys.stderr)
                    backgroundcolor="on_red"

        if options.b:
            foregroundcolor="white"
            backgroundcolor="on_black"
        if options.x:
            if lastbg==backgroundcolor and lastfg==foregroundcolor:
                output+=character
            else:
                if not j==options.startx:
                    output+="</i>"
                output+="""<i class="{} {}">{}""".format(foregroundcolor,backgroundcolor,character)
            if j==linewidth:
                output+="</i>"
        elif options.s:
            if lastbg==backgroundcolor and lastfg==foregroundcolor:
                outputfg+=character
                outputbg+=block
            else:
                if not j==options.startx:
                    outputfg+=svglineend
                    outputbg+=svglineend
                yshift=movedown + (((i-options.starty)+1)*(scale*hshift))
                xshift=moveright+ (((j-options.startx)  )*(scale*wshift))
                text="""<text y="{}" x="{}" style="fill:{{}}">""".format(yshift,xshift)
                outputfg+="""{}{}""".format(text.format(hexcolors[foregroundcolor]),character)
                outputbg+="""{}{}""".format(text.format(hexcolors[backgroundcolor]),block)
            if j==linewidth:
                outputfg+=svglineend
                outputbg+=svglineend
        elif options.i:
            pos="{},{}".format(((j-options.startx)*scale*wshift)-1,0)
            im[i].append("-fill '{}'".format(hexcolors[backgroundcolor]))
            im[i].append("-draw \"text {} '█'\"".format(pos))
            im[i].append("-fill '{}'".format(hexcolors[foregroundcolor]))
            quote=""
            if character in ["'","`"]:
                quote="\\"
            im[i].append("-draw \"text {} '{}{}'\"".format(pos,quote,character))
        else:
            if lastbg is not backgroundcolor or lastfg is not foregroundcolor:
                output+=globals()[foregroundcolor]+globals()[backgroundcolor]
            output+=character
        lastbg=backgroundcolor
        lastfg=foregroundcolor
        lastc=c
        lastcharacter=character
    if options.i:
        number=str(i).zfill(10)
        im[i].append("-write commands/{}_image_{}.png".format(build,number))
        with open("commands/{}_line_{}".format(build,number), "w") as file:
            file.write("\n".join(im[i]))

    if j > 0:
        if not options.v:
            if options.x:
                output+="<br />"
            elif options.s:
                pass
            elif options.i:
                pass
            else:
                output+=reset+"\n"
if options.x:
    output+=htmlend
    if not options.v:
        print(output)
elif options.s:
    output+="\n"+outputbg+"\n"
    output+="\n"+outputfg+"\n"
    output+=svgend
    if not options.v:
        print(output)
elif options.i:
    print(build)
elif not options.v:
    print(output)
