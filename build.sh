dependencies+=('imagemagick')
dependencies+=('coreutils')
dependencies+=('make')
dependencies+=('python3')
dependencies+=('ttf-dejavu')
dependencies+=('ffmpeg')
dependencies+=('gcc')
dependencies+=('python3-dev')
buildcommands[master]="
export NOPROGRESS=true;
git branch -D builder||:;
git checkout -b builder;
make clean;
make test all tiles -j4;
git add --all;
git commit -m 'dist updated by builder' --no-gpg-sign;git push -f origin builder"
