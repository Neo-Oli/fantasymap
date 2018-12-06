#!/usr/bin/env python3
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
import configparser


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

objects={}
objectsini = configparser.ConfigParser()
objectsini.read('objects.ini')
for section in objectsini.sections():
    objects[section]={}
    for option in objectsini[section]:
        objects[section][option]=objectsini[section][option][1:-1]


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
    linewidth=min([len(charsinline)-1,options.endx])
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


        if charsinline[0:j].count("(")>charsinline[0:j+1].count(")"):
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
