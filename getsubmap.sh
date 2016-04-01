python cutmapfile.py $@ > .tempmap.map
python map.py .tempmap.map
rm .tempmap.map

