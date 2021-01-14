#!/bin/bash
commits=`git log --pretty=format:'%H' --all --reverse`
old=""
for c in $commits;do
    for name in map.map mapfile.map map;do
        map="`git show --encoding="UTF-8" $c:$name 2>/dev/null`"
        if [ "$?" == 0 ];then
            break
        fi
    done
    if [ "$map" != "" ];then
        if [ "$map" != "$old" ];then
            old="$map"
            date="`git show -s --format=%ci $c 2>/dev/null`"
            timestamp="`date +%s --date="$date"`"
            filename="history/${timestamp}"
            if [ ! -f "${filename}.map" ];then
                mkdir -p history
                echo "$map" > "${filename}.map"
            fi
            if ! python3 -c "open(\"${filename}.map\",\"r\").read()";then
                echo "Error: File ${filename}.map not readable"
                exit 1
            fi
        fi
    else
        echo error at $c
    fi
done
