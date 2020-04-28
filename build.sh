dependencies+=('imagemagick')
dependencies+=('make')
dependencies+=('python3')
dependencies+=('optipng')
dependencies+=('ttf-dejavu')
buildcommands[master]="git branch -D builder||:;git checkout -b builder;make clean;make -j4 tiles all;git add --allt;git commit -m 'dist updated by builder';git push -f origin builder"
