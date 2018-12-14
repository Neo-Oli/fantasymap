#!/usr/bin/env python3
import os
import re
import sys
import argparse
from uuid import uuid4
import configparser

big=1000000000

def findObject(name, objects):
    for c in objects:
        if objects[c]["name"]==name:
            return c
    print("Error: Object not found with name: {}".format(name),file=sys.stderr)

def config(filename):
    obj={}
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config = configparser.ConfigParser()
    config.read("{}/{}".format(dir_path,filename))
    for section in config.sections():
        obj[section]={}
        for option in config[section]:
            value=config[section][option]
            if isinstance(value,str):
                value=value[1:-1]
            value=value.replace("\\033","\033")
            obj[section][option]=value
    return obj

def legend():
    map="===(Legend for Mapmakers)===#test\n"
    objects=config('objects.ini')
    for key in objects:
        o=objects[key]
        if key in ["(",")"]:
            #don't start a label
            continue
        map+="({}) {} ({})\n".format(key,key,o["name"])
    render(map)
def vim():
    output="setlocal nowrap\n"
    output="{}setlocal redrawtime=10000".format(output)
    objects=config('objects.ini')
    colors=config('colors.ini')
    i=0
    for c in objects:
        rule="rule_{}".format(i)
        match="syn match {} /[{}]/".format(rule,c)
        try:
            fg=colors["vim"][objects[c]["color"]]
            bg=colors["vim"][objects[c]["bgcolor"]]
        except KeyError:
            fg="None"
            bg="None"
        hi="hi def {} ctermfg={} ctermbg={}".format(rule,fg,bg)
        output="{}\n{}\n{}".format(output,match,hi);
        i+=1
    print(output)
def main():
    parser = argparse.ArgumentParser()
    parser.description="Best viewed when piped into `less -RS`"
    parser.add_argument('file', help='Mapfile')
    parser.add_argument('-x', action='store_true', help='print HTML instead of ANSI')
    parser.add_argument('-v', action='store_true', help='Do not print anything. Usefull for checking for errors in the mapfile')
    parser.add_argument('-b', action='store_true', help='Don\'t print color')
    parser.add_argument('-V', action='store_true', help='Print vim ftplugin file')
    parser.add_argument('-i', action='store_true', help='Create png image')
    parser.add_argument('-s', action='store_true', help='Create svg image')
    parser.add_argument('-l', action='store_true', help='Show Mapmakers legend')


    parser.add_argument('starty', type=int, help='Start Y', nargs="?", default=0)
    parser.add_argument('startx', type=int, help='Start X', nargs="?", default=0)
    parser.add_argument('endy', type=int, help='End Y', nargs="?", default=big)
    parser.add_argument('endx', type=int, help='End X', nargs="?", default=big)
    parser.add_argument('-S', type=float, help='font size for several rendering methods', nargs="?", default=10)

    options = parser.parse_args()

    if options.V:
        vim()
    elif options.l:
        legend()
    else:

        with open (options.file, "r") as myfile:
            map=myfile.read()

        mode="ansi"
        if options.x:
            mode="html"
        if options.v:
            mode="none"
        if options.i:
            mode="png"
        if options.s:
            mode="svg"
        render(map, mode,        options.b,        options.startx, options.endx, options.starty,     options.endy,     options.S)
def render(map, mode="ansi", monochrome=False, startx=0,       endx=big,       starty=0, endy=big, scale="12"):
    block="█"
    build=uuid4()
    output=""
    # endy=endy-1
    # endx=endx-1
    objects=config('objects.ini')
    colors=config('colors.ini')

    lines=map.split('\n')
    del lines[-1] # delete last, empty line
    height=len(lines)
    width=len(lines[0].split("#")[0])
    argheight=endy-starty
    argheight+=1
    if argheight!=big:
        height=argheight
    argwidth=endx-startx
    argwidth+=1
    if argwidth!=big:
        width=argwidth




    if mode=="html":
        with open ("map.css", "r") as myfile:
            css=myfile.read()
        csscolors=""
        for key in colors["hex"]:
            prefix=""
            if "on_" in key:
                prefix="background-"
            color=".map .{}{{{}color:{};}}".format(key,prefix,colors["hex"][key])
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
        htmlstart="""{}
            <div class="map">""".format(htmlstart)
        htmlend="""
            </div>
            {}""".format(htmlend)
        output+=htmlstart









    elif mode=="svg":
        wshift=0.6
        hshift=1.15
        movedown=-0.3*scale
        moveright=0*scale
        picheight=height*(scale*hshift)
        picwidth=width*(scale*wshift)

        outputbg=""
        outputfg=""
        svgstart="""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}px" height="{}px" viewBox="0 0 {} {}" style="letter-spacing:0em;font-size:{}px;font-family:&apos;DejaVu Sans Mono&apos;;stroke:none">
    """.format(picwidth,picheight,picwidth,picheight,scale)
        svgend="""</svg>"""

        svglineend="</text>\n"
        output+=svgstart



    elif mode=="png":
        wshift=0.5755
        hshift=1.15

        picheight=round((height*scale*hshift)-1)
        picwidth=round(width*scale*wshift)
        im=[
                "#!/usr/bin/env magick-script",
                # "-monitor",
                "-size {}x{}".format(picwidth,picheight),
                "xc:white",
                "-font DejaVu-Sans-mono",
                "-pointsize {}".format(scale),
                "-gravity NorthWest"
                ]

    map=None
    i=-1
    for line in lines:
        i+=1
        if i<starty:
            continue
        if i>endy:
            continue
        if line=="":
            continue
        charsinline=list(line)
        linewidth=min([len(charsinline)-1,endx])
        j=-1
        lastc=""
        lastfg=""
        lastbg=""
        for c in charsinline:
            j+=1
            if j<startx:
                continue
            if j>endx:
                continue


            if c=="#":
                #close all i tags
                if j>startx:
                    if mode=="html":
                        output+="</i>"
                    if mode=="svg":
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
                        downtrue=downc in list("§rc⁰³⁴⁶⁷⁸")
                        lefttrue=leftc in list("=rC⁰²⁴⁵⁶⁸")
                        righttrue=rightc in list("=rC⁰¹³⁵⁶⁷")
                    else:
                        uptrue=upc in list("x+|!012578jC⁰¹²⁵⁷⁸")
                        downtrue=downc in list("x+!|034678jC⁰³⁴⁶⁷⁸")
                        lefttrue=leftc in list("x+~-024568qc⁰²⁴⁵⁶⁸")
                        righttrue=rightc in list("x+~-013567qc⁰¹³⁵⁶⁷")
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
                    c=findObject(prefix.format(p), objects)
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
                    # the output of set must be sorted otherwise it's order is essentially random, causing different results for max if the array has the same number of two elements
                    backgroundcolor=max(sorted(set(allcolors)), key=allcolors.count)
                if backgroundcolor=="s_average":
                    if "bgcolor_fallback" in objects[c]:
                        backgroundcolor=objects[c]["bgcolor_fallback"]
                    else:
                        print("\nError at line:{}:{} c={}: Coulnd't determine background color".format(str(i+1),str(j+1),c),file=sys.stderr)
                        backgroundcolor="on_red"

            if monochrome:
                foregroundcolor="white"
                backgroundcolor="on_black"
            if mode=="html":
                if lastbg==backgroundcolor and lastfg==foregroundcolor:
                    output+=character
                else:
                    if not j==startx:
                        output+="</i>"
                    output+="""<i class="{} {}">{}""".format(foregroundcolor,backgroundcolor,character)
                if j==linewidth:
                    output+="</i>"
            elif mode=="svg":
                if lastbg==backgroundcolor and lastfg==foregroundcolor:
                    outputfg+=character
                    outputbg+=block
                else:
                    if not j==startx:
                        outputfg+=svglineend
                        outputbg+=svglineend
                    yshift=movedown + (((i-starty)+1)*(scale*hshift))
                    xshift=moveright+ (((j-startx)  )*(scale*wshift))
                    text="""<text y="{}" x="{}" style="fill:{{}}">""".format(yshift,xshift)
                    outputfg+="""{}{}""".format(text.format(colors["hex"][foregroundcolor]),character)
                    outputbg+="""{}{}""".format(text.format(colors["hex"][backgroundcolor]),block)
                if j==linewidth:
                    outputfg+=svglineend
                    outputbg+=svglineend
            elif mode=="png":
                pos="{},{}".format(((j-startx)*scale*wshift)-1,((i-starty)*scale*hshift)-1)
                im.append("-fill '{}'".format(colors["hex"][backgroundcolor]))
                im.append("-draw \"text {} '█'\"".format(pos))
                im.append("-fill '{}'".format(colors["hex"][foregroundcolor]))
                quote=""
                if character in ["'","`"]:
                    quote="\\"
                im.append("-draw \"text {} '{}{}'\"".format(pos,quote,character))
            elif mode=="ansi":
                if lastbg is not backgroundcolor or lastfg is not foregroundcolor:
                    output+=colors["ansi"][foregroundcolor]+colors["ansi"][backgroundcolor]

                output+=character
            lastbg=backgroundcolor
            lastfg=foregroundcolor
            lastc=c
            lastcharacter=character
        if j > 0:
            if mode=="html":
                output+="<br />"
            elif mode=="svg":
                pass
            elif mode=="png":
                pass
            elif mode=="ansi":
                output+=colors["ansi"]["reset"]+"\n"
    if mode=="html":
        output+=htmlend
        print(output)
    elif mode=="svg":
        output+="\n"+outputbg+"\n"
        output+="\n"+outputfg+"\n"
        output+=svgend
        print(output)
    elif mode=="png":
        im.append("-crop {}x{}+0+0".format(picwidth-1,picheight))
        im.append("-write png:-")
        print("\n".join(im))
    elif mode=="ansi":
        print(output[0:-1]) #cut off trailing newline

main()
