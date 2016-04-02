#!/usr/bin/env python3
import re, sys, argparse
parser = argparse.ArgumentParser()
parser.description="Best viewed when piped into `less -RS`"
parser.add_argument('file', help='Mapfile')
parser.add_argument('-x', action='store_true', help='print HTML instead of ANSI')
parser.add_argument('-v', action='store_true', help='Do not print anything. Usefull for checking for errors in the mapfile')
options = parser.parse_args()


with open (options.file, "r") as myfile:
    map=myfile.read()



objects={}
objects['w']={}
objects['w']['name']="water"
objects['w']['r']="▓"
objects['w']['color']="blue"
objects['w']['bgcolor']="on_black"

objects[',']={}
objects[',']['name']="sand"
objects[',']['r']="▓"
objects[',']['color']="yellow"
objects[',']['bgcolor']="on_black"

objects['.']={}
objects['.']['name']="grass"
objects['.']['r']="░"
objects['.']['color']="green"
objects['.']['bgcolor']="on_black"

objects['i']={}
objects['i']['name']="snow"
objects['i']['r']="▓"
objects['i']['color']="iwhite"
objects['i']['bgcolor']="on_black"

objects['s']={}
objects['s']['name']="street"
objects['s']['r']="█"
objects['s']['color']="biwhite"
objects['s']['bgcolor']="on_black"


objects['y']={}
objects['y']['name']="farmland"
objects['y']['r']="▓"
objects['y']['color']="yellow"
objects['y']['bgcolor']="on_black"
objects['y']['xggpmcolor']="#AA9106"

objects['a']={}
objects['a']['name']="forrest"
objects['a']['r']="♣"
objects['a']['color']="bigreen"
objects['a']['bgcolor']="on_black"

objects['ä']={}
objects['ä']['name']="forrest2"
objects['ä']['r']="♠"
objects['ä']['color']="bigreen"
objects['ä']['bgcolor']="on_black"

objects['à']={}
objects['à']['name']="palmforrest"
objects['à']['r']="Γ"
objects['à']['color']="bigreen"
objects['à']['bgcolor']="on_black"

objects['b']={}
objects['b']['name']="building"
objects['b']['r']="▪"
objects['b']['color']="biblack"
objects['b']['bgcolor']="on_black"

objects['B']={}
objects['B']['name']="multiblock_building"
objects['B']['r']="█"
objects['B']['color']="biblack"
objects['B']['bgcolor']="on_black"

objects['L']={}
objects['L']['name']="special_building_lighthouse"
objects['L']['r']="◘"
objects['L']['color']="ired"
objects['L']['bgcolor']="on_black"


objects['m']={}
objects['m']['name']="mountain"
objects['m']['r']="▲"
objects['m']['color']="iblack"
objects['m']['bgcolor']="on_black"

objects['0']={}
objects['0']['name']="street_crossing"
objects['0']['r']="┼"
objects['0']['color']="biwhite"
objects['0']['bgcolor']="on_black"

objects['-']={}
objects['-']['name']="street_h"
objects['-']['r']="─"
objects['-']['color']="biwhite"
objects['-']['bgcolor']="on_black"

objects['|']={}
objects['|']['name']="street_v"
objects['|']['r']="│"
objects['|']['color']="biwhite"
objects['|']['bgcolor']="on_black"

objects['1']={}
objects['1']['name']="street_c1"
objects['1']['r']="┐"
objects['1']['color']="biwhite"
objects['1']['bgcolor']="on_black"

objects['2']={}
objects['2']['name']="street_c2"
objects['2']['r']="┌"
objects['2']['color']="biwhite"
objects['2']['bgcolor']="on_black"

objects['3']={}
objects['3']['name']="street_c3"
objects['3']['r']="┘"
objects['3']['color']="biwhite"
objects['3']['bgcolor']="on_black"

objects['4']={}
objects['4']['name']="street_c4"
objects['4']['r']="└"
objects['4']['color']="biwhite"
objects['4']['bgcolor']="on_black"

objects['5']={}
objects['5']['name']="street_c5"
objects['5']['r']="┬"
objects['5']['color']="biwhite"
objects['5']['bgcolor']="on_black"

objects['6']={}
objects['6']['name']="street_c6"
objects['6']['r']="┴"
objects['6']['color']="biwhite"
objects['6']['bgcolor']="on_black"

objects['7']={}
objects['7']['name']="street_c7"
objects['7']['r']="┤"
objects['7']['color']="biwhite"
objects['7']['bgcolor']="on_black"

objects['8']={}
objects['8']['name']="street_c8"
objects['8']['r']="├"
objects['8']['color']="biwhite"
objects['8']['bgcolor']="on_black"

objects['9']={}
objects['9']['name']="street_none"
objects['9']['r']="▪"
objects['9']['color']="biwhite"
objects['9']['bgcolor']="on_black"




objects['0r']={}
objects['0r']['name']="rails_crossing"
objects['0r']['r']="╬"
objects['0r']['color']="bired"
objects['0r']['bgcolor']="on_black"

objects['-r']={}
objects['-r']['name']="rails_h"
objects['-r']['r']="═"
objects['-r']['color']="bired"
objects['-r']['bgcolor']="on_black"

objects['|r']={}
objects['|r']['name']="rails_v"
objects['|r']['r']="║"
objects['|r']['color']="bired"
objects['|r']['bgcolor']="on_black"

objects['1r']={}
objects['1r']['name']="rails_c1"
objects['1r']['r']="╗"
objects['1r']['color']="bired"
objects['1r']['bgcolor']="on_black"

objects['2r']={}
objects['2r']['name']="rails_c2"
objects['2r']['r']="╔"
objects['2r']['color']="bired"
objects['2r']['bgcolor']="on_black"

objects['3r']={}
objects['3r']['name']="rails_c3"
objects['3r']['r']="╝"
objects['3r']['color']="bired"
objects['3r']['bgcolor']="on_black"

objects['4r']={}
objects['4r']['name']="rails_c4"
objects['4r']['r']="╚"
objects['4r']['color']="bired"
objects['4r']['bgcolor']="on_black"

objects['5r']={}
objects['5r']['name']="rails_c5"
objects['5r']['r']="╦"
objects['5r']['color']="bired"
objects['5r']['bgcolor']="on_black"

objects['6r']={}
objects['6r']['name']="rails_c6"
objects['6r']['r']="╩"
objects['6r']['color']="bired"
objects['6r']['bgcolor']="on_black"

objects['7r']={}
objects['7r']['name']="rails_c7"
objects['7r']['r']="╣"
objects['7r']['color']="bired"
objects['7r']['bgcolor']="on_black"

objects['8r']={}
objects['8r']['name']="rails_c8"
objects['8r']['r']="╠"
objects['8r']['color']="bired"
objects['8r']['bgcolor']="on_black"

objects['9r']={}
objects['9r']['name']="rails_none"
objects['9r']['r']="▪"
objects['9r']['color']="bired"
objects['9r']['bgcolor']="on_black"


objects['[']={}
objects['[']['name']="street-rails-crossing-horizontal"
objects['[']['r']="╫"
objects['[']['color']="bired"
objects['[']['bgcolor']="on_black"


objects[']']={}
objects[']']['name']="street-rails-crossing-vertical"
objects[']']['r']="╪"
objects[']']['color']="bired"
objects[']']['bgcolor']="on_black"

objects['j']={}
objects['j']['name']="bridgev"
objects['j']['r']="║"
objects['j']['color']="white"
objects['j']['bgcolor']="on_blue"

objects['q']={}
objects['q']['name']="bridgeh"
objects['q']['r']="═"
objects['q']['color']="white"
objects['q']['bgcolor']="on_blue"

objects['p']={}
objects['p']['name']="pool"
objects['p']['r']="▐"
objects['p']['color']="blue"
objects['p']['bgcolor']="on_black"

objects['o']={}
objects['o']['name']="pond"
objects['o']['r']="●"
objects['o']['color']="blue"
objects['o']['bgcolor']="on_black"

objects[' ']={}
objects[' ']['name']="empty"
objects[' ']['r']=" "
objects[' ']['color']="empty"
objects[' ']['bgcolor']="on_black"



empty="";reset='\033[0m';black='\033[0;30m';red='\033[0;31m';green='\033[0;32m';yellow='\033[0;33m';blue='\033[0;34m';purple='\033[0;35m';cyan='\033[0;36m';white='\033[0;37m';bblack='\033[1;30m';bred='\033[1;31m';bgreen='\033[1;32m';byellow='\033[1;33m';bblue='\033[1;34m';bpurple='\033[1;35m';bcyan='\033[1;36m';bwhite='\033[1;37m';ublack='\033[4;30m';ured='\033[4;31m';ugreen='\033[4;32m';uyellow='\033[4;33m';ublue='\033[4;34m';upurple='\033[4;35m';ucyan='\033[4;36m';uwhite='\033[4;37m';on_black='\033[40m';on_red='\033[41m';on_green='\033[42m';on_yellow='\033[43m';on_blue='\033[44m';on_purple='\033[45m';on_cyan='\033[46m';on_white='\033[47m';iblack='\033[0;90m';ired='\033[0;91m';igreen='\033[0;92m';iyellow='\033[0;93m';iblue='\033[0;94m';ipurple='\033[0;95m';icyan='\033[0;96m';iwhite='\033[0;97m';biblack='\033[1;90m';bired='\033[1;91m';bigreen='\033[1;92m';biyellow='\033[1;93m';biblue='\033[1;94m';bipurple='\033[1;95m';bicyan='\033[1;96m';biwhite='\033[1;97m';on_iblack='\033[0;100m';on_ired='\033[0;101m';on_igreen='\033[0;102m';on_iyellow='\033[0;103m';on_iblue='\033[0;104m';on_ipurple='\033[0;105m';on_icyan='\033[0;106m';on_iwhite='\033[0;107m';on_biblack='\033[1;100m';on_bired='\033[1;101m';on_bigreen='\033[1;102m';on_biyellow='\033[1;103m';on_biblue='\033[1;104m';on_bipurple='\033[1;105m';on_bicyan='\033[1;106m';on_biwhite='\033[1;107m';


htmlstart="""
<!DOCTYPE html><html><head><meta charset="UTF-8"><style type="text/css">@import url(https://fonts.googleapis.com/css?family=Roboto+Mono);
body{white-space:nowrap;margin:0}i{line-height:16px;font-family:'Roboto Mono',monospace;margin:0;vertical-align:top;display:inline-block;white-space:pre;height:20px;font-size:18px;text-align:center;font-style:normal}br:first-child{display:none}.black{color:#282828}.red{color:#cc241d}.green{color:#98971a}.yellow{color:#d79921}.blue{color:#458588}.purple{color:#689d6a}.cyan{color:#689d6a}.white{color:#a89985}.bblack{color:#282828}.bred{color:#cc241d}.bgreen{color:#98971a}.byellow{color:#d79921}.bblue{color:#458588}.bpurple{color:#689d6a}.bcyan{color:#689d6a}.bwhite{color:#a89985}.ublack{color:#282828}.ured{color:#cc241d}.ugreen{color:#98971a}.uyellow{color:#d79921}.ublue{color:#458588}.upurple{color:#689d6a}.ucyan{color:#689d6a}.uwhite{color:#a89985}.on_black{background-color:#282828}.on_red{background-color:#cc241d}.on_green{background-color:#98971a}.on_yellow{background-color:#d79921}.on_blue{background-color:#458588}.on_purple{background-color:#689d6a}.on_cyan{background-color:#689d6a}.on_white{background-color:#a89985}.iblack{color:#928379}.ired{color:#fb4934}.igreen{color:#b8bb26}.iyellow{color:#fabd2f}.iblue{color:#83a590}.ipurple{color:#d3869b}.icyan{color:#8ec07c}.iwhite{color:#ebdbb2}.biblack{color:#928379}.bired{color:#fb4934}.bigreen{color:#b8bb26}.biyellow{color:#fabd2f}.biblue{color:#83a590}.bipurple{color:#d3869b}.bicyan{color:#8ec07c}.biwhite{color:#ebdbb2}.on_iblack{background-color:#282828}.on_ired{background-color:#cc241d}.on_igreen{background-color:#98971a}.on_iyellow{background-color:#d79921}.on_iblue{background-color:#458588}.on_ipurple{background-color:#689d6a}.on_icyan{background-color:#689d6a}.on_iwhite{background-color:#a89985}.on_biblack{background-color:#928375}.on_bired{background-color:#fb4934}.on_bigreen{background-color:#b8bb26}.on_biyellow{background-color:#fabd2f}.on_biblue{background-color:#83a590}.on_bipurple{background-color:#d3869b}.on_bicyan{background-color:#8ec07c}.on_biwhite{background-color:#ebdbb2}
</style></head><body class="on_black">
"""
htmlend="</body></html>"

lines=map.split('\n')
if options.x:
    if not options.v:
        print(htmlstart)
map=None
i=0
label=False
for line in lines:
    charsinline=list(line)
    j=0
    lastc=""
    lastfg=""
    lastbg=""
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
        # This is just for speed. It will work without it.
        # It probably doesn't matter now, that that while loop is gone.
        elif c==lastc and c!="x":
            character=lastcharacter
            backgroundcolor=lastbg
            foregroundcolor=lastfg
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
                if not options.v:
                    print(character, end="")
            else:
                if not j==0:
                    if not options.v:
                        print("</i>",end="")
                if not options.v:
                    print("<i class=\""+foregroundcolor+" "+backgroundcolor+"\">"+character, end="")
            if j==len(charsinline)-1:
                if not options.v:
                    print("</i>",end="")
        else:
            if lastbg is not backgroundcolor or lastfg is not foregroundcolor:
                if not options.v:
                    print(globals()[foregroundcolor]+globals()[backgroundcolor],end="")
            if not options.v:
                print(character, end="")
        lastbg=backgroundcolor
        lastfg=foregroundcolor
        lastc=c
        lastcharacter=character
        j+=1
    if options.x:
        if not options.v:
            print("<br />",end="")
    else:
        if not options.v:
            print(reset)
    i+=1
if options.x:
    if not options.v:
        print(htmlend)

