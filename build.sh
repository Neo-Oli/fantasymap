dependencies+=('imagemagick')
dependencies+=('coreutils')
dependencies+=('make')
dependencies+=('python3')
dependencies+=('optipng')
dependencies+=('ttf-dejavu')
dependencies+=('ffmpeg')
buildcommands[master]="
export NOPROGRESS=true;
git branch -D builder||:;
git checkout -b builder;
make clean;
make test all tiles -j4;
git add --all;
git commit -m 'dist updated by builder';git push -f origin builder"
