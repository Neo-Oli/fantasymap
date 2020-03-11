dependencies+=('imagemagick')
dependencies+=('make')
dependencies+=('python3')
dependencies+=('optipng')
dependencies+=('ttf-dejavu')
buildcommands[ANY]="[ \"\`git log -1 --pretty=format:'%an'\`\" != 'Glow Builder' ] && make -j4 tiles all;git add dist;git commit -m 'dist updated by builder';git push origin HEAD:$branch"
