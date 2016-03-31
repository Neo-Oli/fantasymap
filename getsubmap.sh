cat mapfile.map | sed -n $1,$(echo "$1+$2-1"|bc)p |  sed "s/^.\{$3\}//g" | sed -r "s/^(.{$4}).*/\1/" > .tempmap.map
python map.py .tempmap.map
rm .tempmap.map

