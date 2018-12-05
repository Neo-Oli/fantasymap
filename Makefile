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
	@rm -fvr commands

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

REQ := recipes/%.rec map.py map.map
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
	@mkdir -p commands build
	build=`./map.py -iS 3 map.map \`cat $<\``;\
	echo $${build};\
	chmod +x commands/$${build}_line_*;\
	ls commands/$${build}_line_* | parallel -j4 --bar {};\
	montage -font DejaVu-Sans commands/$${build}_image_* $${f} -geometry +0 -tile 1x commands/$${build}_stitched.png;\
	mv commands/$${build}_stitched.png $@;\
	rm commands/$${build}_*
	@rmdir --ignore-fail-on-non-empty commands

