#!/usr/bin/env python3
import sys
import configparser

with open(sys.argv[1], "r") as f:
    config_string = "[DEFAULT]\n" + f.read()
config = configparser.ConfigParser()
config.read_string(config_string)
conf = config["DEFAULT"]
if "args" in conf:
    print(conf.get("args"))
    sys.exit(0)
mapfile = "map.map"
with open(mapfile, "r") as mapfile:
    map = mapfile.read()
lines = map.split("\n")
for y in range(0, len(lines)):
    line = lines[y]
    x = line.find(conf.get("name"))
    if x >= 0:
        print(
            "{} {} {} {}".format(
                y + int(conf.get("source_y",
                                 0)),
                x + int(conf.get("source_x",
                                 -1)),
                y + int(conf.get("height",
                                 10)),
                x + int(conf.get("width",
                                 len(conf.get("name")))),
            )
        )
        sys.exit(0)
sys.exit(1)
