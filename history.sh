#!/bin/bash
commits=`git log --pretty=format:'%H' --all --reverse`
old=""
for c in $commits;do
    for name in map.map mapfile.map map;do
        git show $c:$name 2>/dev/null > history/temp
        if ! python3 -c "open(\"history/temp\",\"r\").read()";then
            git show --encoding="UTF-8" $c:$name 2>/dev/null > history/temp
            if ! python3 -c "open(\"history/temp\",\"r\").read()";then
                echo "Error: File ${filename}.map not readable"
                exit 1
            fi
        fi
        map=$(<history/temp)
        if [ -n "$map" ];then
            break
        fi
    done
    if [ "$map" != "" ];then
        if [ "$map" != "$old" ];then
            old="$map"
            date="`git show -s --encoding="UTF-8" --format=%ci $c 2>/dev/null`"
            echo $date
            timestamp="`date +%s --date="$date"`"
            filename="history/${timestamp}"
            if [ ! -f "${filename}.map" ];then
                mkdir -p history
                mv history/temp "${filename}.map"
            fi
        fi
    else
        echo error at $c
    fi
done
rm -f history/temp
