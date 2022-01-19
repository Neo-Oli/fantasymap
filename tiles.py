#!/usr/bin/env python3
import os
import os.path
import math
from pathlib import Path
from shutil import copyfile

# import hashlib
def write(filename, content):
    # h="#{}\n".format(hashlib.md5(content.encode("utf-8")).hexdigest())
    # with open(filename,"r") as file:
    # oldh=file.readline()
    # if oldh == h:
    # return
    # content="{}{}".format(h,content)
    with open(filename, "w") as file:
        file.write(content)
    print("{} written".format(filename))

os.system("mkdir -p dist/tilescripts")

xi = 10
yi = 5
z = 9
mapfile = "map.map"
cachemapfile = "dist/tilescripts/cache.map"
with open(mapfile, "r") as myfile:
    map = myfile.read()
try:
    with open(cachemapfile, "r") as myfile:
        cachemap = myfile.read()
except FileNotFoundError:
    cachemap = ""
lines = map.split("\n")
clines = cachemap.split("\n")
files = os.listdir("dist/tilescripts/")

del lines[-1]  # delete last, empty line
del clines[-1]  # delete last, empty line
h = len(lines)
w = len(lines[0].split("#")[0])
for i in range(0, h, yi):
    for y in range(0, yi):
        try:
            line = lines[i + y]
            cline = clines[i + y]
        except IndexError:
            line = ""
            cline = ""
        charsinline = list(line)
        ccharsinline = list(cline)
        for j in range(0, w, xi):
            old = "".join(charsinline[j:j + xi])
            try:
                new = "".join(ccharsinline[j:j + xi])
            except IndexError:
                new = ""
            xm = round(j / xi)
            ym = round(i / yi)
            name = "{}-{}-{}".format(z, xm, ym)
            webpname = "{}/{}/{}.webp".format(z, xm, ym)
            cachename = "{}.cache".format(name)
            magickname = "{}.magick".format(name)
            if cachename not in files or old != new:
                print("{} changed".format(name))
                Path("dist/tilescripts/{}".format(cachename)).touch()
            else:
                print("{}".format(name))
                if magickname in files:
                    Path("dist/tilescripts/{}".format(magickname)).touch()
                try:
                    Path("dist/tiles/{}".format(webpname)).touch()
                except FileNotFoundError:
                    pass

copyfile(mapfile, cachemapfile)
magick = []
webp = []
stitched = []
i = 0
for y in range(0, h, yi):
    j = 0
    for x in range(0, w, xi):
        xx = x + xi
        yy = y + yi
        xm = round(x / xi)
        ym = round(y / yi)
        name = "{}-{}-{}".format(z, xm, ym)
        cachefile = "{}.cache".format(name)
        newpath = "../tiles/{}/{}/{}.webp".format(z, xm, ym)
        file = "{}.magick".format(name)
        magick.append("{}: {}".format(file, cachefile))
        magick.append("\t@echo Building $@")
        magick.append('\t@if [ ! -f "$@" ];then touch "$@";fi;\\')
        magick.append("\t. ../../VENV/bin/activate;\\")
        magick.append(
            '\tres="`../../map.py -iS 44.7 ../../map.map {} {} {} {}`";\\'.format(
                y,
                x,
                yy - 1,
                xx - 1
            )
        )
        magick.append('\thash="#`echo \\"$$res\\"|md5sum`";\\')
        magick.append('\tif [ "$$hash" != "`head -n1 $@`" ]; then \\')
        magick.append('\t\techo "$$hash" > $@;\\')
        magick.append('\t\techo "$$res" >> $@;\\')
        magick.append("\telse \\")
        magick.append("\t\ttouch -r $@ $<;\\")
        magick.append("\tfi")
        webp.append("{}: {}".format(newpath, file))
        webp.append("\t@echo Building $@")
        webp.append('\t@mkdir -p "../tiles/{}/{}"'.format(z, xm))
        webp.append("\t@magick-script $< > $@")
        j += 1
    i += 1

newi = i
newj = j
z -= 1
noimg = "xc:none"
for zoom in range(z, 0, -1):
    i = newi
    j = newj
    newi = 0
    for y in range(0, i, 2):
        newj = 0
        for x in range(0, j, 2):
            path = "../tiles/{}".format(zoom + 1)
            newpath = "../tiles/{}/{}/{}.webp".format(zoom, round(x / 2), round(y / 2))
            im = [
                "{}/{}/{}.webp".format(path,
                                      x,
                                      y),
                "{}/{}/{}.webp".format(path,
                                      x + 1,
                                      y),
                "{}/{}/{}.webp".format(path,
                                      x,
                                      y + 1),
                "{}/{}/{}.webp".format(path,
                                      x + 1,
                                      y + 1),
            ]
            ie = im[:]
            if x >= j - 1:
                im[1] = noimg
                im[3] = noimg
                ie[1] = ""
                ie[3] = ""
            if y >= i - 1:
                im[2] = noimg
                im[3] = noimg
                ie[2] = ""
                ie[3] = ""
            stitched.append("{}: {} {} {} {}".format(newpath, ie[0], ie[1], ie[2], ie[3]))
            stitched.append("\t@echo Building $@")
            stitched.append('\t@mkdir -p "../tiles/{}/{}";\\'.format(zoom, round(x / 2)))
            name = "{}-{}-{}".format(zoom, round(x / 2), round(y / 2))
            stitched.append(
                "\tmontage -font DejaVu-Sans -background none {} {} {} {} -geometry 128x128 -tile 2x $@"
                .format(im[0],
                        im[1],
                        im[2],
                        im[3])
            )
            stitched.append("\t@optiwebp $@ 2> /dev/null")
            newj += 1
        newi += 1

filename = "dist/tilescripts/Makefile"

makefile = """
.PHONY: tiles
tiles: ../tiles/1/0/0.webp
{}
{}
{}
""".format("\n".join(magick),
           "\n".join(webp),
           "\n".join(stitched))
write(filename, makefile)
