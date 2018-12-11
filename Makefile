define display
	less -RS "$(1)"
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

ALL := \
$(subst recipes,build,$(subst .rec,.ansi,$(wildcard recipes/*)))\
$(subst recipes,build,$(subst .rec,-monochrome.ansi,$(wildcard recipes/*)))\
$(subst recipes,build,$(subst .rec,.html,$(wildcard recipes/*)))\
$(subst recipes,build,$(subst .rec,-monochrome.html,$(wildcard recipes/*)))\
$(subst recipes,build,$(subst .rec,.svg,$(wildcard recipes/*)))\
$(subst recipes,build,$(subst .rec,-monochrome.svg,$(wildcard recipes/*)))\

.PHONY: all
all: $(ALL) tiles

.PHONY: help
help: build/legend
	$(call display,$<)
build/legend: legend.map map.py
	./map.py legend.map > "$@"
BASE := map.py map.map
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
build/%.png: $(REQ)
	@mkdir -p build
	./map.py -iS 22.35 map.map `cat $<` > $@.magick
	echo -write png:$@ >> $@.magick
	magick-script ./$@.magick




.PHONY: tiles
tiles:
	./tiles.py
	make $(MFLAGS) -C build/tilescripts
