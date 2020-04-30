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
	make -B dist/${COMP}.ansi;\
	clear;\
	while true; do \
		tput civis;\
		printf "\033[41mOld\n";\
		echo "$$old";\
		tput cnorm;\
		sleep 1;\
		tput cup 0 0;\
		printf "\033[42mNew\n";\
		make -s dist/${COMP}.ansi;\
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

.PHONY: all
all: $(ALL) dist/index.js

dist/recipes/%: recipes/%.rec
	cp -vr recipes dist/recipes

dist/index.js: $(ALL) dist/tiles/1/0/0.png
	cd dist;\
		find -type f |\
		grep -v 'vimrc$$'|\
		grep -v 'tilescripts'|\
		xargs -I _ echo "import '_'" \
		> index.js

BASE := map.py map.map objects.ini colors.ini
REQ := recipes/%.rec $(BASE)
.PRECIOUS: dist/%
dist/%.html: $(REQ)
	@mkdir -p dist
	./map.py -x map.map `cat $<` > $@
dist/%-monochrome.html: $(REQ)
	@mkdir -p dist
	./map.py -xb map.map `cat $<` > $@
dist/%-monochrome.ansi: $(REQ)
	@mkdir -p dist
	./map.py -b map.map `cat $<` > $@
dist/%.svg: $(REQ)
	@mkdir -p dist
	./map.py -s map.map `cat $<` > $@
dist/%-monochrome.svg: $(REQ)
	@mkdir -p dist
	./map.py -sb map.map `cat $<` > $@
dist/%.ansi: $(REQ)
	@mkdir -p dist
	./map.py map.map `cat $<` > $@
dist/%.txt: $(REQ)
	@mkdir -p dist
	./map.py -t map.map `cat $<` > $@
dist/%.png: $(REQ)
	@mkdir -p dist
	./map.py -iS 22.35 map.map `cat $<` | magick-script - > $@
dist/%-monochrome.png: $(REQ)
	@mkdir -p dist
	./map.py -biS 22.35 map.map `cat $<` | magick-script - > $@
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

linenum := $(patsubst %,dist/lines/%.ansi,$(shell seq -f %05g 000 499))

dist/lines/%.ansi: dist/lines/%.txt
	rec=$$(basename $<|cut -d'.' -f1);\
	./map.py map.map $$rec 0 $$rec 10000 > $@

.PHONY: _fast
dist/fast.ansi: $(linenum)
	cat $(linenum) > $@


.PHONY: _fast
_fast:
	make _fast_source
	make $(MFLAGS) dist/fast.ansi
.PHONY: fast
fast: _fast
	$(call display,dist/fast.ansi)

.PHONY: tiles
tiles: dist/tiles/1/0/0.png
dist/tiles/1/0/0.png: $(BASE) tiles.py
	./tiles.py
	make $(MFLAGS) -C dist/tilescripts

.PHONY: lint
lint: VENV/pyvenv.cfg
	. VENV/bin/activate;\
	black map.py

VENV/pyvenv.cfg: requirements.txt
	python3 -m venv VENV
	. VENV/bin/activate;\
	pip install -r requirements.txt
