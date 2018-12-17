define display
	less -RSF "$(1)"
endef


.PHONY: whole
whole: build/whole.ansi
	$(call display,$<)

%: build/%.ansi
	$(call display,$<)

m-%: build/%-monochrome.ansi
	$(call display,$<)

.PHONY: edit
edit: build/vimrc
	$(EDITOR) map.map -c ":so build/vimrc"

build/vimrc: map.py
	mkdir -p build
	./map.py -V /dev/null > "$@"

.PHONY: clean
clean:
	@rm -fvr build
	@rm -fvr .make-*

ALL := \
$(subst recipes,build,$(subst .rec,.ansi,$(wildcard recipes/*)))\
$(subst recipes,build,$(subst .rec,.txt,$(wildcard recipes/*)))\
$(subst recipes,build,$(subst .rec,-monochrome.ansi,$(wildcard recipes/*)))\
$(subst recipes,build,$(subst .rec,.html,$(wildcard recipes/*)))\
$(subst recipes,build,$(subst .rec,-monochrome.html,$(wildcard recipes/*)))\
$(subst recipes,build,$(subst .rec,.svg,$(wildcard recipes/*)))\
$(subst recipes,build,$(subst .rec,-monochrome.svg,$(wildcard recipes/*)))\
$(filter-out build/whole.png, $(subst recipes,build,$(subst .rec,.png,$(wildcard recipes/*))))\
$(filter-out build/whole-monochrome.png, $(subst recipes,build,$(subst .rec,-monochrome.png,$(wildcard recipes/*))))\

.PHONY: all
all: $(ALL)

.PHONY: help
help: build/help.ansi
	$(call display,$<)
BASE := map.py map.map objects.ini colors.ini
REQ := recipes/%.rec $(BASE)
.PRECIOUS: build/%
build/%.html: $(REQ)
	@mkdir -p build
	./map.py -x map.map `cat $<` > $@
build/%-monochrome.html: $(REQ)
	@mkdir -p build
	./map.py -xb map.map `cat $<` > $@
build/%-monochrome.ansi: $(REQ)
	@mkdir -p build
	./map.py -b map.map `cat $<` > $@
build/%.svg: $(REQ)
	@mkdir -p build
	./map.py -s map.map `cat $<` > $@
build/%-monochrome.svg: $(REQ)
	@mkdir -p build
	./map.py -sb map.map `cat $<` > $@
build/%.ansi: $(REQ)
	@mkdir -p build
	./map.py map.map `cat $<` > $@
build/%.txt: $(REQ)
	@mkdir -p build
	./map.py -t map.map `cat $<` > $@
build/%.png: $(REQ)
	@mkdir -p build
	./map.py -iS 22.35 map.map `cat $<` | magick-script - > $@
build/%-monochrome.png: $(REQ)
	@mkdir -p build
	./map.py -biS 22.35 map.map `cat $<` | magick-script - > $@




.PHONY: tiles
tiles: build/tiles/1/0/0.png
build/tiles/1/0/0.png: $(BASE) tiles.py
	./tiles.py
	make $(MFLAGS) -C build/tilescripts
