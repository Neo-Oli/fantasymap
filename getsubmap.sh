#!/bin/sh
python3 cutmapfile.py $@ > .tempmap.map
python3 map.py .tempmap.map
rm .tempmap.map

