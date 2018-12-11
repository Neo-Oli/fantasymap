#!/usr/bin/env python
import os
import math
# import hashlib
def write(filename,content):
    # h="#{}\n".format(hashlib.md5(content.encode("utf-8")).hexdigest())
    # with open(filename,"r") as file:
        # oldh=file.readline()
    # if oldh == h:
        # return
    # content="{}{}".format(h,content)
    with open(filename, "w") as file:
        file.write(content)
    print("{} written".format(filename))
os.system("mkdir -p build/tilescripts")

w=1000
h=500

xi=20
yi=10
z=6
i=0
files={}
files[z]=[]
for y in range(0,h,yi):
    j=0
    for x in range(0,w,xi):
        xx=x+xi
        yy=y+yi
        xm=round(x/xi)
        ym=round(y/yi)
        name="{}-{}-{}".format(z,xm,ym)
        newpath="build/tiles/{}/{}/{}.png".format(z,xm,ym)
        files[z].append([z,xm,ym])
        command="cd ../..;"
        command+="mkdir -p build/tiles/{}/{};".format(z,xm)
        command+="res=\"`./map.py -iS 22.35 map.map {} {} {} {}`\";".format(y,x,yy,xx)
        # command+="echo \"#`echo \"$res\"|md5sum`\" > build/tilescripts/{}.magick;".format(name)
        command+="echo \"$res\" > build/tilescripts/{}.magick;".format(name)
        command+="echo -write png:{} >> build/tilescripts/{}.magick;".format(newpath,name)
        command+="magick-script build/tilescripts/{}.magick".format(name)
        filename="build/tilescripts/{}.sh".format(name)
        write(filename,command)
        j+=1
    i+=1

newi=i
newj=j
z-=1
for zoom in range(z,0, -1):
    i=newi
    j=newj
    newi=0
    files[zoom]=[]
    for y in range(0,i,2):
        newj=0
        for x in range(0,j,2):
            path="build/tiles/{}".format(zoom+1)
            command="cd ../..;"
            command+="i1={}/{}/{}.png;\n".format(path,x  ,y  )
            command+="i2={}/{}/{}.png;\n".format(path,x+1,y  )
            command+="i3={}/{}/{}.png;\n".format(path,x  ,y+1)
            command+="i4={}/{}/{}.png;\n".format(path,x+1,y+1)
            name="{}-{}-{}".format(zoom,round(x/2),round(y/2))
            newpath="build/tiles/{}/{}/{}.png".format(zoom,round(x/2),round(y/2))
            files[zoom].append([zoom,round(x/2),round(y/2)])
            command+="mkdir -p build/tiles/{}/{};\n".format(zoom,round(x/2))
            for var in range(1,5):
                command+="if [ ! -f \"$i{}\" ];then i{}=\"xc:none\";fi;\n".format(var,var)
            command+="montage -font DejaVu-Sans $i1 $i2 $i3 $i4 -geometry 128x128 -tile 2x {};\n".format(newpath)
            filename="build/tilescripts/{}.sh".format(name)
            write(filename,command)
            newj+=1
        newi+=1


m=".PHONY: tiles\n"
m+="tiles:\n"
for zoom in range(z+1,0, -1):
    m+="\t make $(MFLAGS) tiles{}\n".format(zoom)


for zoom in range(z+1,0, -1):
    m+="TILES{} := $(sort $(subst -,/,$(subst tilescripts,tiles,$(subst .sh,.png,$(wildcard ../tilescripts/{}-*.sh)))))\n".format(zoom,zoom)
    m+=".PHONY: tiles{}\n".format(zoom)
    m+="tiles{}: $(TILES{})\n".format(zoom,zoom)
    for f in files[zoom]:
        m+="../tiles/{}/{}/{}.png: {}-{}-{}.sh\n".format(f[0],f[1],f[2],f[0],f[1],f[2])
        m+="\tsh $<\n"
filename="build/tilescripts/Makefile"
write(filename,m)
