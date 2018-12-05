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
all: $(ALL)

.PHONY: help
help: build/legend
	$(call display,$<)
build/legend: legend.map map.py
	./map.py legend.map > "$@"

.PRECIOUS: build/%.ansi build/%.map
build/%.map: recipes/%.rec map.map map.py
	mkdir -p build
	./cutmapfile.py map.map `cat $<` > "$@"
build/%.html: build/%.map
	./map.py -x $< > $@
build/%-monochrome.html: build/%.map
	./map.py -xb $< > $@
build/%-monochrome.ansi: build/%.map
	./map.py -b $< > $@
build/%.svg: build/%.map
	./map.py -i $< > $@
build/%-monochrome.svg: build/%.map
	./map.py -ib $< > $@
build/%.ansi: build/%.map
	./map.py $< > $@
