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

xi=19
yi=9
z=7
i=0
magick=[]
png=[]
stitched=[]
for y in range(0,h,yi):
    j=0
    for x in range(0,w,xi):
        xx=x+xi
        yy=y+yi
        xm=round(x/xi)
        ym=round(y/yi)
        name="{}-{}-{}".format(z,xm,ym)
        newpath="../tiles/{}/{}/{}.png".format(z,xm,ym)
        file="{}.magick".format(name)
        magick.append("{}: ../../map.py ../../map.map ../../objects.ini ../../colors.ini".format(file))
        # magick.append("\t@echo Building $@")
        magick.append("\t@if [ ! -f \"$@\" ];then touch \"$@\";fi;\\")
        magick.append("\tres=\"`../../map.py -iS 22.35 ../../map.map {} {} {} {}`\";\\".format(y,x,yy,xx))
        magick.append("\thash=\"#`echo \\\"$$res\\\"|md5sum`\";\\")
        magick.append("\tif [ \"$$hash\" != \"`head -n1 $@`\" ]; then \\")
        magick.append("\t\techo \"$$hash\\n$$res\" > $@;\\")
        magick.append("\t\techo -n \"#\";\\")
        magick.append("\telse \\")
        magick.append("\t\techo -n \".\";\\")
        magick.append("\tfi")
        png.append("{}: {}".format(newpath,file))
        png.append("\t@echo Building $@")
        png.append("\t@mkdir -p \"../tiles/{}/{}\"".format(z,xm))
        png.append("\t@magick-script $< > $@")
        j+=1
    i+=1

newi=i
newj=j
z-=1
noimg="xc:none"
for zoom in range(z,0, -1):
    i=newi
    j=newj
    newi=0
    for y in range(0,i,2):
        newj=0
        for x in range(0,j,2):
            path="../tiles/{}".format(zoom+1)
            newpath="../tiles/{}/{}/{}.png".format(zoom,round(x/2),round(y/2))
            im=[
                "{}/{}/{}.png".format(path,x  ,y  ),
                "{}/{}/{}.png".format(path,x+1,y  ),
                "{}/{}/{}.png".format(path,x  ,y+1),
                "{}/{}/{}.png".format(path,x+1,y+1)
                ]
            ie=im[:]
            if x>=j-1:
                im[1]=noimg
                im[3]=noimg
                ie[1]=""
                ie[3]=""
            if y>=i-1:
                im[2]=noimg
                im[3]=noimg
                ie[2]=""
                ie[3]=""
            stitched.append("{}: {} {} {} {}".format(newpath,ie[0],ie[1],ie[2],ie[3]))
            stitched.append("\t@echo Building $@")
            stitched.append("\t@mkdir -p \"../tiles/{}/{}\";\\".format(zoom,round(x/2)))
            name="{}-{}-{}".format(zoom,round(x/2),round(y/2))
            stitched.append("\tmontage -font DejaVu-Sans {} {} {} {} -geometry 128x128 -tile 2x $@".format(im[0],im[1],im[2],im[3]))
            newj+=1
        newi+=1


filename="build/tilescripts/Makefile"

makefile="""
.PHONY: tiles
tiles: ../tiles/1/0/0.png
{}
{}
{}
""".format(
        "\n".join(magick),
        "\n".join(png),
        "\n".join(stitched)
        )
write(filename,makefile)
