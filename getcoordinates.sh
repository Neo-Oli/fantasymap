cat mapfile.map | sed -n $1,$2p | cut -c $3-$4 > .tempmap.map
python map.py .tempmap.map
rm .tempmap.map

