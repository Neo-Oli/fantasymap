define display
	less -RSF "$(1)"
endef


.PHONY: whole
whole: dist/whole.ansi
	$(call display,$<)

%: dist/%.ansi
	$(call display,$<)

m-%: dist/%-monochrome.ansi
	$(call display,$<)

16-%: dist/%-16color.ansi
	$(call display,$<)

i-%: dist/%.png
	feh $<

.PHONY: edit
edit: dist/vimrc
	$(EDITOR) map.map -c ":so dist/vimrc"

dist/vimrc: map.py
	mkdir -p dist
	./map.py -V /dev/null > "$@"

.PHONY: clean
clean:
	@rm -fvr dist

.PHONY: compare
COMP ?= oogle
compare:
	git checkout dist/${COMP}.ansi
	old="`cat dist/${COMP}.ansi`";\
	$(MAKE) -B dist/${COMP}.ansi;\
	clear;\
	while true; do \
		tput civis;\
		printf "\033[41mOld\n";\
		echo "$$old";\
		tput cnorm;\
		sleep 1;\
		tput cup 0 0;\
		printf "\033[42mNew\n";\
		$(MAKE) -s dist/${COMP}.ansi;\
		tput civis;\
		cat dist/${COMP}.ansi;\
		tput cnorm;\
		sleep 1;\
		tput cup 0 0;\
	done

ALL := \
$(subst recipes,dist,$(subst .rec,.ansi,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,.txt,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,-monochrome.ansi,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,-16color.ansi,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,.html,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,-monochrome.html,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,.svg,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,-monochrome.svg,$(wildcard recipes/*)))\
$(subst recipes,dist/recipes,$(wildcard recipes/*))\
$(filter-out dist/whole.png, $(subst recipes,dist,$(subst .rec,.png,$(wildcard recipes/*))))\
$(filter-out dist/whole-monochrome.png, $(subst recipes,dist,$(subst .rec,-monochrome.png,$(wildcard recipes/*))))\
dist/recipes\
dist/vimrc\
_fast

HISTORY := \
	$(subst history,dist/history,$(subst .map,.svg,$(wildcard history/*)))\
	$(subst history,dist/history,$(subst .map,.png,$(wildcard history/*)))\
	dist/history/history.webm
.PHONY: all
all: $(ALL) dist/index.js $(HISTORY)

dist/recipes/%: recipes/%.rec
	cp -vr recipes dist/recipes

dist/index.js: $(ALL) dist/tiles/1/0/0.png
	cd dist;\
		find -type f |\
		grep -v 'vimrc$$'|\
		grep -v '\/tilescripts\/'|\
		grep -v '\/lines\/'|\
		sort|\
		sed -e "s/^/import '/" -e "s/$$/'/" \
		> index.js

BASE := map.py map.map objects.json colors.json getCoordinates.py
REQ := recipes/%.rec $(BASE)
.PRECIOUS: dist/%
dist/%.html: $(REQ)
	@mkdir -p dist
	./map.py -x map.map `./getCoordinates.py $<` > $@
dist/%-monochrome.html: $(REQ)
	@mkdir -p dist
	./map.py -xb map.map `./getCoordinates.py $<` > $@
dist/%-monochrome.ansi: $(REQ)
	@mkdir -p dist
	./map.py -b map.map `./getCoordinates.py $<` > $@
dist/%-16color.ansi: $(REQ)
	@mkdir -p dist
	./map.py -T map.map `./getCoordinates.py $<` > $@
dist/%.svg: $(REQ)
	@mkdir -p dist
	./map.py -s map.map `./getCoordinates.py $<` > $@
dist/%-monochrome.svg: $(REQ)
	@mkdir -p dist
	./map.py -sb map.map `./getCoordinates.py $<` > $@
dist/%.ansi: $(REQ)
	@mkdir -p dist
	./map.py map.map `./getCoordinates.py $<` > $@
dist/%.txt: $(REQ)
	@mkdir -p dist
	./map.py -t map.map `./getCoordinates.py $<` > $@
dist/%.png: $(REQ)
	@mkdir -p dist
	./map.py -iS 22.35 map.map `./getCoordinates.py $<` | magick-script - > $@
dist/%-monochrome.png: $(REQ)
	@mkdir -p dist
	./map.py -biS 22.35 map.map `./getCoordinates.py $<` | magick-script - > $@
dist/recipes/%.rec: $(REQ)
	@mkdir -p dist/recipes
	cp $< $@



.PHONY: _fast_source
_fast_source: $(BASE)
	mkdir -p dist/lines
	i=0;\
	while read line; do \
		linename=$$(printf "%05d" $$i);\
		old="";\
		if [ -f dist/lines/$${linename}.txt ];then \
			old=$$(cat dist/lines/$${linename}.txt);\
		fi;\
		if [ "$$old" != "$$line" ];then \
			echo "$$line" > dist/lines/$${linename}.txt;\
			echo "updated line $${linename}.txt";\
		else\
			if [ -f dist/lines/$${linename}.ansi ]; then \
				touch -r dist/lines/$${linename}.txt dist/lines/$${linename}.ansi;\
			fi;\
		fi;\
		i=$$((i+1));\
	done < map.map

linenum := $(patsubst %,dist/lines/%.ansi,$(shell seq -f %05g 000 $$(cat map.map|wc -l)))

dist/lines/%.ansi: dist/lines/%.txt
	rec=$$(basename $<|cut -d'.' -f1);\
	./map.py map.map $$rec 0 $$rec 10000 > $@

.PHONY: _fast
dist/fast.ansi: $(linenum)
	cat $(linenum) > $@


.PHONY: _fast
_fast:
	$(MAKE) _fast_source
	$(MAKE) dist/fast.ansi
.PHONY: fast
fast: _fast
	$(call display,dist/fast.ansi)

.PHONY: tiles
tiles: dist/tiles/1/0/0.png
dist/tiles/1/0/0.png: $(BASE) tiles.py
	./tiles.py
	$(MAKE) -C dist/tilescripts

.PHONY: lint
lint: VENV/pyvenv.cfg
	. VENV/bin/activate;\
	black *.py
	for f in *.json; do \
		echo $$f;\
		jq -M . $$f > $$f.pretty&&\
		mv $$f.pretty $$f;\
	done

VENV/pyvenv.cfg: requirements.txt
	python3 -m venv VENV
	. VENV/bin/activate;\
	pip install -r requirements.txt

.PHONY: history-sources
history-sources:
	./history.sh
.PHONY: history
history: $(HISTORY)

dist/history/history.webm: $(HISTORY)
	ffmpeg -y -r 5 -pattern_type glob -i 'dist/history/*.png' $@

dist/history/%.svg: history/%.map $(BASE)
	@mkdir -p dist/history
	./map.py -q -s $< > $@

dist/history/%.png: dist/history/%.svg $(BASE)
	@mkdir -p dist/history
	source=history/$$(basename $< .svg).map;\
	width=$$(echo -n "$$(head -n1 "$$source"|sed 's/#.*$$//' )"|wc -m);\
	width=$$((width*2));\
	height=$$(cat "$$source"|wc -l);\
	height=$$((height*4));\
	echo $${width}x$${height}
	convert -size $${width}x$${height} $< $@

test: $(subst .sh,.sh.tested,$(wildcard tests/*))

tests/%.sh.tested: tests/%.sh
	./$<
