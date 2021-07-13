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
	. VENV/bin/activate;\
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
dist/history/history.webm\
dist/whole-small.png\

HISTORY := \
	$(subst history,dist/history,$(subst .map,.svg,$(wildcard history/*)))\
	$(subst history,dist/history,$(subst .map,.png,$(wildcard history/*)))

.PHONY: all
all: $(ALL) dist/index.js

dist/recipes/%: recipes/%.rec
	cp -vr recipes dist/recipes

dist/index.js: $(ALL) dist/tiles/1/0/0.png
	cd dist;\
		(\
		find -type f |\
		grep -v 'vimrc$$'|\
		grep -v '\/tilescripts\/'|\
		grep -v '\/lines\/'|\
		grep -v '\/history\/'|\
		grep -v '\/fast.ansi';\
		echo ./history/history.webm;\
		)|\
		sort|\
		sed -e "s/^/import '/" -e "s/$$/'/" \
		> index.js

BASE := map.py map.map objects.json colors.json getCoordinates.py VENV/pyvenv.cfg
REQ := recipes/%.rec $(BASE)
.PRECIOUS: dist/%
dist/%.html: $(REQ)
	@mkdir -p dist
	. VENV/bin/activate;\
	./map.py -x map.map `./getCoordinates.py $<` > $@
dist/%-monochrome.html: $(REQ)
	@mkdir -p dist
	. VENV/bin/activate;\
	./map.py -xb map.map `./getCoordinates.py $<` > $@
dist/%-monochrome.ansi: $(REQ)
	@mkdir -p dist
	. VENV/bin/activate;\
	./map.py -b map.map `./getCoordinates.py $<` > $@
dist/%-16color.ansi: $(REQ)
	@mkdir -p dist
	. VENV/bin/activate;\
	./map.py -T map.map `./getCoordinates.py $<` > $@
dist/%.svg: $(REQ)
	@mkdir -p dist
	. VENV/bin/activate;\
	./map.py -s map.map `./getCoordinates.py $<` > $@
dist/%-monochrome.svg: $(REQ)
	@mkdir -p dist
	. VENV/bin/activate;\
	./map.py -sb map.map `./getCoordinates.py $<` > $@
dist/%.ansi: $(REQ)
	@mkdir -p dist
	. VENV/bin/activate;\
	./map.py map.map `./getCoordinates.py $<` > $@
dist/%.txt: $(REQ)
	@mkdir -p dist
	. VENV/bin/activate;\
	./map.py -t map.map `./getCoordinates.py $<` > $@
dist/%.png: $(REQ)
	@mkdir -p dist
	. VENV/bin/activate;\
	./map.py -iS 22.35 map.map `./getCoordinates.py $<` | magick-script - > $@
dist/%-monochrome.png: $(REQ)
	@mkdir -p dist
	. VENV/bin/activate;\
	./map.py -biS 22.35 map.map `./getCoordinates.py $<` | magick-script - > $@
dist/recipes/%.rec: $(REQ)
	@mkdir -p dist/recipes
	cp $< $@

linenum := $(patsubst %,dist/lines/%.ansi,$(shell seq -f %05g 1 $$(cat map.map|wc -l)))

dist/lines:
	mkdir -p $@
dist/lines/%.ansi: $(BASE) dist/lines
	. VENV/bin/activate;\
	rec=$$(basename $@|cut -d'.' -f1| sed 's/^0*//');\
	coord="$$((rec - 1))";\
	start=$$((rec-1));\
	end=$$((rec+1));\
	if [ "$$start" -lt "1" ]; then \
		start=1;\
	fi;\
	line=$$(sed -n "$${start},$${end}p" map.map);\
	if [ -f "$@.cache" ];then \
		old="$$(cat $@.cache)";\
	fi;\
	if [ "$${line}" != "$$old" ];then \
		./map.py map.map $$coord 0 $$coord 10000 > $@;\
		echo "$$line" > $@.cache;\
	else \
		if [ -f $@ ];then \
			touch $@;\
		fi;\
	fi

dist/fast.ansi: $(linenum)
	cat $(linenum) > $@

.PHONY: fast
fast: dist/fast.ansi
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
history: dist/history/history.webm

.INTERMEDIATE: dist/history/input.txt
dist/history/input.txt: $(HISTORY)
	for f in dist/history/*.png;do \
		last=$$f;\
	done;\
	for f in dist/history/*.png;do \
		if [ "$$f" != "$$last" ];then \
			echo "file '$$(basename $$f)'";\
			echo "duration 1";\
		else \
			echo "file '$$(basename $$f)'";\
			echo "duration 5";\
			echo "file '$$(basename $$f)'";\
		fi;\
	done > $@

dist/history/history.webm: dist/history/input.txt
	ffmpeg -y -f concat -i $< -vf fps=30 $@

dist/history/%.svg: history/%.map $(BASE)
	@mkdir -p dist/history
	. VENV/bin/activate;\
	./map.py -q -s $< > $@

dist/history/%.png: dist/history/%.svg $(BASE)
	@mkdir -p dist/history
	source=history/$$(basename $< .svg).map;\
	width=$$(echo -n "$$(head -n1 "$$source"|sed 's/#.*$$//' )"|wc -m);\
	height=$$(cat "$$source"|wc -l);\
	height=$$((height*2));\
	echo $${width}x$${height}
	convert -size $${width}x$${height} $< -resize 1920x1080 -background black -gravity center -extent 1920x1080 $@

dist/whole-small.png: dist/whole.svg $(BASE)
	source=map.map;\
	width=$$(echo -n "$$(head -n1 "$$source"|sed 's/#.*$$//' )"|wc -m);\
	height=$$(cat "$$source"|wc -l);\
	height=$$((height*2));\
	echo $${width}x$${height}
	convert -size $${width}x$${height} $< -resize 1920x1080 -background black -gravity center -extent 1920x1080 $@

test: $(subst .sh,.sh.tested,$(wildcard tests/*))

tests/%.sh.tested: tests/%.sh $(BASE)
	. VENV/bin/activate;\
	./$<
