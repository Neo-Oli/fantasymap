#!/usr/bin/env python3
import os
import re
import sys
import argparse
from uuid import uuid4
import configparser
import math
from collections import Counter

big = 1000000000
heightstretch = 2


def config(filename):
    obj = {}
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config = configparser.ConfigParser()
    config.read("{}/{}".format(dir_path, filename))
    for section in config.sections():
        obj[section] = {}
        for option in config[section]:
            value = config[section][option]
            if isinstance(value, str):
                value = value[1:-1]
            value = value.replace("\\033", "\033")
            obj[section][option] = value
            if option in ["average_ignore_type", "connects", "connections", "r"]:
                obj[section][option] = obj[section][option].split(",")
                for key, val in enumerate(obj[section][option]):
                    obj[section][option][key] = val.strip()
    return obj


def error(err):
    print(err, file=sys.stderr)


def progress(done, ultimate):
    if "NOPROGRESS" not in os.environ:
        if ultimate == 0:
            return
        width = 50
        bar = ""
        percentage = math.floor((done / ultimate) * 100)
        if done % 1000 == 0 or percentage == 100:
            for i in range(0, width):
                if (i / width) * 100 <= percentage:
                    bar += "="
                else:
                    bar += " "
            print(
                "\r[{}] {}% {}/{}".format(bar, percentage, done, ultimate),
                file=sys.stderr,
                end="",
            )


def findObjects(name, objects, fields=["name"]):
    obj = []
    for c in objects:
        for field in fields:
            if field in objects[c]:
                if objects[c][field] == name:
                    obj.append(c)
    return obj


def legend():
    map = "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr#test\n"
    map += "r(        Legend for Mapmakers        )r\n"
    map += "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr\n"
    objects = config("objects.ini")
    for key in objects:
        o = objects[key]
        if key in ["(", ")"] or len(key) > 1:
            # don't start a label
            continue
        map += "({}){}({})\n".format(key, key, o["name"])
    return map


def vim():
    output = "setlocal nowrap\n"
    output = "{}setlocal redrawtime=10000".format(output)
    objects = config("objects.ini")
    colors = config("colors.ini")
    i = 0
    for c in objects:
        rule = "rule_{}".format(i)
        match = "syn match {} /[{}]/".format(rule, c)
        try:
            fg = colors["vim"][objects[c]["color"]]
            bg = colors["vim"][objects[c]["bgcolor"]]
        except KeyError:
            fg = "None"
            bg = "None"
        hi = "hi def {} ctermfg={} ctermbg={}".format(rule, fg, bg)
        output = "{}\n{}\n{}".format(output, match, hi)
        i += 1
    print(output)


def isNear(grid, i, j, fields, values, radius=5):
    for y in range(i - radius, i + radius):
        for x in range(j - radius, j + radius):
            if (
                math.sqrt(math.pow((x - j), 2) + math.pow((y - i) * heightstretch, 2))
                < radius
            ):
                if x == j and y == i:
                    continue
                else:
                    try:
                        c = objects[grid[y][x]]
                        for field in fields:
                            if c[field] in values:
                                if grid[y][0:x].count("(") <= grid[y][0 : x + 1].count(
                                    ")"
                                ):
                                    return True
                    except IndexError:
                        pass
                    except KeyError:
                        pass


def isLabel(grid, y, x):
    return grid[y][0:x].count("(") > grid[y][0 : x + 1].count(")")


def hexToRGB(color):
    color = color.lstrip("#")
    return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))


def main():
    parser = argparse.ArgumentParser()
    parser.description = "Best viewed when piped into `less -RS`"
    parser.add_argument("file", help="Mapfile")
    parser.add_argument("-x", action="store_true", help="print HTML instead of ANSI")
    parser.add_argument(
        "-v",
        action="store_true",
        help="Do not print anything. Usefull for checking for errors in the mapfile",
    )
    parser.add_argument("-b", action="store_true", help="Don't print color")
    parser.add_argument("-V", action="store_true", help="Print vim ftplugin file")
    parser.add_argument("-i", action="store_true", help="Create png image")
    parser.add_argument("-s", action="store_true", help="Create svg image")
    parser.add_argument("-l", action="store_true", help="Show Mapmakers legend")
    parser.add_argument("-T", action="store_true", help="Disable true color ansi")
    parser.add_argument(
        "-t", action="store_true", help="Output input text (cuts map file)"
    )

    parser.add_argument("starty", type=int, help="Start Y", nargs="?", default=0)
    parser.add_argument("startx", type=int, help="Start X", nargs="?", default=0)
    parser.add_argument("endy", type=int, help="End Y", nargs="?", default=big)
    parser.add_argument("endx", type=int, help="End X", nargs="?", default=big)
    parser.add_argument(
        "-S",
        type=float,
        help="font size for several rendering methods",
        nargs="?",
        default=10,
    )

    options = parser.parse_args()

    if options.V:
        vim()
    else:

        with open(options.file, "r") as myfile:
            map = myfile.read()

        if options.l:
            map = legend()

        mode = "ansi"
        if options.x:
            mode = "html"
        if options.v:
            mode = "none"
        if options.i:
            mode = "png"
        if options.s:
            mode = "svg"
        if options.t:
            mode = "txt"
        output = render(
            map,
            mode,
            options.b,
            options.startx,
            options.endx,
            options.starty,
            options.endy,
            options.S,
            not options.T,
        )
        display(output)


def render(
    map,
    mode="ansi",
    monochrome=False,
    startx=0,
    endx=big,
    starty=0,
    endy=big,
    scale="12",
    truecolor=False,
):
    block = "█"
    build = uuid4()
    output = {}
    output["prefix"] = ""
    output["fg"] = {}
    output["bg"] = {}
    output["postfix"] = ""
    # endy=endy-1
    # endx=endx-1

    grid = map.split("\n")
    del grid[-1]  # delete last, empty line
    height = len(grid)
    wholeheight = height
    width = len(grid[0].split("#")[0])
    for key, line in enumerate(grid):
        grid[key] = list(line.split("#")[0])
    wholewidth = width
    argheight = endy - starty
    argheight += 1
    argwidth = endx - startx
    argwidth += 1
    if endx != big or endy != big or startx != 0 or starty != 0:
        if argheight <= height:
            height = argheight
        if argwidth <= width:
            width = argwidth

    if mode == "html":
        with open("map.css", "r") as myfile:
            css = myfile.read()
        csscolors = ""
        for key in colors["hex"]:
            prefix = ""
            if "on_" in key:
                prefix = "background-"
            color = ".map .{}{{{}color:{};}}".format(key, prefix, colors["hex"][key])
            csscolors = "{}{}".format(csscolors, color)
        htmlstart = """
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
        <style>
        {}
        {}
        </style>
        </head>
        <body>""".format(
            css, csscolors
        )
        htmlend = """
        </body>
    </html>"""
        htmlstart = """{}
            <div class="map">""".format(
            htmlstart
        )
        htmlend = """
            </div>
            {}""".format(
            htmlend
        )
        output["prefix"] = htmlstart

    elif mode == "svg":
        wshift = 0.6
        hshift = 1.15
        movedown = -0.3 * scale
        moveright = 0 * scale
        picheight = height * (scale * hshift)
        picwidth = width * (scale * wshift)

        outputbg = ""
        outputfg = ""
        svgstart = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}px" height="{}px" viewBox="0 0 {} {}" style="letter-spacing:0em;font-size:{}px;font-family:&apos;DejaVu Sans Mono&apos;;stroke:none">
    """.format(
            picwidth, picheight, picwidth, picheight, scale
        )
        svgend = """</svg>"""

        svglineend = "</text>\n"
        output["prefix"] = svgstart

    elif mode == "png":
        wshift = 0.5755
        hshift = 1.15

        picheight = round((height * scale * hshift) - 1)
        picwidth = round((width * scale * wshift) + 1)
        output["prefix"] = "\n".join(
            [
                "#!/usr/bin/env magick-script",
                # "-monitor",
                "-size {}x{}".format(picwidth, picheight),
                "xc:none",
                "-font DejaVu-Sans-mono",
                "-pointsize {}".format(scale),
                "-gravity NorthWest",
            ]
        )
    output["width"] = wholewidth
    for i in range(0, len(grid)):
        output["height"] = wholeheight
        output["fg"][i] = {}
        output["fg"][i]["prefix"] = ""
        output["fg"][i]["chars"] = {}
        output["fg"][i]["postfix"] = ""
        output["bg"][i] = {}
        output["bg"][i]["prefix"] = ""
        output["bg"][i]["chars"] = {}
        output["bg"][i]["postfix"] = ""
        if i < starty:
            continue
        if i > endy:
            continue
        if grid[i] == "":
            continue
        linewidth = min([len(grid[i]), endx])
        output["width"] = max(output["width"], linewidth)
        lastc = ""
        lastfg = ""
        lastbg = ""
        for j in range(0, len(grid[i])):
            c = grid[i][j]
            backgroundcolor = ""
            foregroundcolor = ""
            cout = ""
            coutbg = ""
            orig = c
            if j < startx:
                continue
            if j > endx:
                continue
            progress((((i - starty) * width) + (j - startx)) + 1, height * width)
            # get the surounding characters

            try:
                leftc = grid[i][j - 1]
            except IndexError:
                leftc = "N"
            try:
                rightc = grid[i][j + 1]
            except IndexError:
                rightc = "N"
            try:
                upc = grid[i - 1][j]
            except IndexError:
                upc = "N"
            try:
                downc = grid[i + 1][j]
            except IndexError:
                downc = "N"
            try:
                upleftc = grid[i - 1][j - 1]
            except IndexError:
                upleftc = "N"
            try:
                uprightc = grid[i - 1][j + 1]
            except IndexError:
                uprightc = "N"

            try:
                downleftc = grid[i + 1][j - 1]
            except IndexError:
                downleftc = "N"
            try:
                downrightc = grid[i + 1][j + 1]
            except IndexError:
                downrightc = "N"

            # Reading from -1 causes wrap
            if j == 0:
                leftc = "N"
            if i == 0:
                upc = "N"
            if isLabel(grid, i, j):
                foregroundcolor = objects["?"]["color"]
                backgroundcolor = objects["?"]["bgcolor"]
                character = c
            else:
                if not c in objects:
                    error(
                        "Error at line:{} char:{} c:{}".format(
                            str(i + 1), str(j + 1), c
                        )
                    )
                    c = "E"
                if c == objectsByName["water"]:
                    if (
                        isNear(
                            grid,
                            i,
                            j,
                            ["name", "type"],
                            ["grass", "sand", "dirt"],
                            5,
                        )
                        or isNear(grid, i, j, ["name", "type"], ["mountain"], 3)
                    ):
                        c = objectsByName["water_shallow"]
                    else:
                        c = objectsByName["water_deep"]
                elif c == objectsByName["forest on grass"]:
                    numtrees_top = 1
                    while (
                        i - numtrees_top > -1
                        and grid[i - numtrees_top][j]
                        == objectsByName["forest on grass"]
                    ):
                        numtrees_top += 1
                    if numtrees_top % 2:
                        if downc == objectsByName["forest on grass"]:
                            numtrees_left = 1
                            while (
                                j - numtrees_left > 0
                                and grid[i][j - numtrees_left]
                                == objectsByName["forest on grass"]
                            ):
                                numtrees_left += 1
                            mod = (numtrees_left - 1) % 4
                            c = objectsByName["tree_top_{}".format(mod)]
                            if upc != objectsByName["forest on grass"]:
                                try:
                                    backgroundcolor = objects[upc]["bgcolor"]
                                except:
                                    pass
                    else:
                        numtrees_right = 1
                        if j + 1 in grid[i]:
                            while (
                                j + numtrees_right <= linewidth
                                and grid[i][j + numtrees_right]
                                == objectsByName["forest on grass"]
                            ):
                                numtrees_right += 1
                        mod = (numtrees_right - 1) % 3
                        c = objectsByName["tree_bottom_{}".format(mod)]
                elif objects[c]["connects"]:
                    nc = ""
                    for ofType in findObjects(objects[c]["name"], objects, ["type"]):
                        if c == ofType:
                            continue
                        cont = False
                        for directions in [
                            ["u", "d", upc],
                            ["d", "u", downc],
                            ["l", "r", leftc],
                            ["r", "l", rightc],
                        ]:
                            connectSelf = directions[0]
                            connectDirection = directions[1]
                            direction = directions[2]
                            try:
                                dirc = objects[direction]
                            except KeyError:
                                dirc = objects["N"]
                            ofc = objects[ofType]
                            if (
                                dirc["name"] in objects[c]["connects"]
                                or dirc["type"] in objects[c]["connects"]
                            ) and (
                                connectDirection in dirc["connections"]
                                or not dirc["connections"]
                            ):
                                if connectSelf not in ofc["connections"]:
                                    cont = True
                                    break
                            else:
                                if connectSelf in ofc["connections"]:
                                    cont = True
                                    break
                        if cont:
                            continue
                        nc = ofType
                    c = nc
                if not c in objects:
                    error(
                        "Error at line:{} char:{} c:{}".format(
                            str(i + 1), str(j + 1), c
                        )
                    )
                    c = "E"
                if not foregroundcolor:
                    foregroundcolor = objects[c]["color"]
                if not backgroundcolor:
                    backgroundcolor = objects[c]["bgcolor"]
                if len(objects[c]["r"]) == 1:
                    character = objects[c]["r"][0]
                else:
                    index = ((j * i) + 1) % len(objects[c]["r"])
                    index = math.floor(math.sin(j) * math.sin(i) * 100000) % len(
                        objects[c]["r"]
                    )
                    character = objects[c]["r"][index]
            radius = 1
            while backgroundcolor == "s_average":
                allcolors = []
                for y in range(i - radius, i + radius + 1):
                    for x in range(j - radius, j + radius + 1):
                        if y == i and x == j:
                            # ignore self
                            continue
                        # if isLabel(grid,y,x):
                        # continue
                        try:
                            f = grid[y][x]
                        except IndexError:
                            continue
                        try:
                            ignored = False
                            if "average_ignore_type" in objects[c]:
                                for ignore in objects[c]["average_ignore_type"]:
                                    if objects[f]["name"] == ignore:
                                        ignored = True
                                    if objects[f]["type"] == ignore:
                                        ignored = True
                            if ignored:
                                continue
                            avcolor = objects[f]["bgcolor"]
                            if "bgcolor_average_overwrite" in objects[f]:
                                avcolor = objects[f]["bgcolor_average_overwrite"]
                            elif "bgcolor_fallback" in objects[f]:
                                avcolor = objects[f]["bgcolor_fallback"]
                            if avcolor != "ignore":
                                allcolors.append(avcolor)
                        except KeyError:
                            pass
                if allcolors:
                    counted = Counter(allcolors).most_common()
                    if c == objectsByName["debugger"]:
                        error("Average Debug: {}".format(counted))
                    if len(counted) == 1 or counted[0][1] != counted[1][1]:
                        backgroundcolor = counted[0][0]
                radius += 1

            if (
                backgroundcolor == "on_{}".format(foregroundcolor)
                and "same_color_fallback" in objects[c]
            ):
                foregroundcolor = objects[c]["same_color_fallback"]
            if monochrome:
                foregroundcolor = "white"
                backgroundcolor = "on_black"
            if mode == "html":
                if lastbg == backgroundcolor and lastfg == foregroundcolor:
                    cout += character
                else:
                    if not j == startx:
                        cout += "</i>"
                    cout += """<i class="{} {}">{}""".format(
                        foregroundcolor, backgroundcolor, character
                    )
                if j + 1 == linewidth:
                    cout += "</i>"
            elif mode == "svg":
                if lastbg == backgroundcolor and lastfg == foregroundcolor:
                    cout += character
                    coutbg += block
                else:
                    if not j == startx:
                        cout += svglineend
                        coutbg += svglineend
                    yshift = movedown + (((i - starty) + 1) * (scale * hshift))
                    xshift = moveright + (((j - startx)) * (scale * wshift))
                    text = """<text y="{}" x="{}" style="fill:{{}}">""".format(
                        yshift, xshift
                    )
                    cout += """{}{}""".format(
                        text.format(colors["hex"][foregroundcolor]), character
                    )
                    coutbg += """{}{}""".format(
                        text.format(colors["hex"][backgroundcolor]), block
                    )
                if j + 1 == linewidth:
                    cout += svglineend
                    coutbg += svglineend
            elif mode == "png":
                posx = (j - startx) * scale * wshift
                posy = (i - starty) * scale * hshift
                pos = "{},{}".format(posx, posy)
                cout += "\n-fill '{}'".format(colors["hex"][backgroundcolor])
                quote = ""
                if character in ["'", "`"]:
                    quote = "\\"
                cout += "\n".join(
                    [
                        "",
                        "-draw \"text {} '█'\"".format(pos),
                        "-fill '{}'".format(colors["hex"][foregroundcolor]),
                        "-draw \"text {} '{}{}'\"".format(pos, quote, character),
                    ]
                )
            elif mode == "txt":
                cout += orig
            elif mode == "ansi":
                if (
                    lastbg is not backgroundcolor or lastfg is not foregroundcolor
                ) and not monochrome:
                    if not truecolor:
                        cout += (
                            colors["ansi"][foregroundcolor]
                            + colors["ansi"][backgroundcolor]
                        )
                    else:
                        r, g, b = hexToRGB(colors["hex"][backgroundcolor])
                        bg = "\x1b[48;2;{};{};{}m".format(r, g, b)
                        r, g, b = hexToRGB(colors["hex"][foregroundcolor])
                        fg = "\x1b[38;2;{};{};{}m".format(r, g, b)
                        cout += fg
                        cout += bg
                cout += character
            lastbg = backgroundcolor
            lastfg = foregroundcolor
            lastc = c
            lastcharacter = character
            output["fg"][i]["chars"][j] = cout
            output["bg"][i]["chars"][j] = coutbg
        if mode == "html":
            output["fg"][i]["postfix"] = "<br />"
        elif mode == "txt":
            output["fg"][i]["postfix"] = "\n"
        elif mode == "ansi":
            if not monochrome:
                output["fg"][i]["postfix"] = "{}\n".format(colors["ansi"]["reset"])
            else:
                output["fg"][i]["postfix"] = "\n"
    if mode == "html":
        output["postfix"] = htmlend
    elif mode == "svg":
        output["postfix"] = svgend
    elif mode == "png":
        output["postfix"] = "\n".join(
            ["", "-crop {}x{}+1+0".format(picwidth - 2, picheight), "-write png:-"]
        )

    return output


def display(output):
    p = output["prefix"]
    for i in range(0, output["height"]):
        p += output["bg"][i]["prefix"]
        for j in range(0, output["width"]):
            try:
                p += output["bg"][i]["chars"][j]
            except KeyError:
                pass
        p += output["bg"][i]["postfix"]
    for i in range(0, output["height"]):
        p += output["fg"][i]["prefix"]
        for j in range(0, output["width"]):
            try:
                p += output["fg"][i]["chars"][j]
            except KeyError:
                pass
        p += output["fg"][i]["postfix"]
    p += output["postfix"]
    print(p.strip())


objects = config("objects.ini")
colors = config("colors.ini")
objectsByName = {}

# get values from type
for c in objects:
    objectsByName[objects[c]["name"]] = c
    if "type" in objects[c]:
        # use findObjects here because objectsByName isn't fully populated yet
        try:
            parent = objects[findObjects(objects[c]["type"], objects)[0]]
        except IndexError:
            error("parent of {} not found".format(objects[c]["name"]))
        new = parent.copy()
        new["connects"] = []  # don't copy connects from parent
        new.update(objects[c])
        objects[c] = new
    else:
        objects[c]["type"] = False
    if "connections" not in objects[c]:
        objects[c]["connections"] = []
    if "connects" not in objects[c]:
        objects[c]["connects"] = []

main()
if "NOPROGRESS" not in os.environ:
    print(file=sys.stderr)
