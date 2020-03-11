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

.PHONY: edit
edit: dist/vimrc
	$(EDITOR) map.map -c ":so dist/vimrc"

dist/vimrc: map.py
	mkdir -p dist
	./map.py -V /dev/null > "$@"

.PHONY: clean
clean:
	@rm -fvr dist

ALL := \
$(subst recipes,dist,$(subst .rec,.ansi,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,.txt,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,-monochrome.ansi,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,.html,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,-monochrome.html,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,.svg,$(wildcard recipes/*)))\
$(subst recipes,dist,$(subst .rec,-monochrome.svg,$(wildcard recipes/*)))\
$(filter-out dist/whole.png, $(subst recipes,dist,$(subst .rec,.png,$(wildcard recipes/*))))\
$(filter-out dist/whole-monochrome.png, $(subst recipes,dist,$(subst .rec,-monochrome.png,$(wildcard recipes/*))))\

.PHONY: all
all: $(ALL)

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




.PHONY: tiles
tiles: dist/tiles/1/0/0.png
dist/tiles/1/0/0.png: $(BASE) tiles.py
	./tiles.py
	make $(MFLAGS) -C dist/tilescripts
