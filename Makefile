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
$(subst recipes,build,$(subst .rec,.png,$(wildcard recipes/*)))\

.PHONY: all
all: $(ALL)

.PHONY: help
help: build/legend
	$(call display,$<)
build/legend: $(REQ)
	./map.py legend.map > "$@"

.PRECIOUS: build/%.ansi build/%.map
build/%.map: recipes/%.rec
	mkdir -p build
	./cutmapfile.py map.map `cat $<` > "$@"
build/%.html: build/%.map
	./map.py -x $< > $@
build/%-monochrome.html: build/%.map
	./map.py -xb $< > $@
build/%-monochrome.ansi: build/%.map
	./map.py -b $< > $@
build/%.png: build/%.map
	mkdir -p commands
	build=`./map.py -i $<`;\
	echo $${build};\
	chmod +x commands/$${build}_line_*;\
	ls commands/$${build}_line_* | parallel -j4 --bar {};\
	montage -font DejaVu-Sans commands/$${build}_image_* -geometry +0 -tile 1x $@;\
	rm commands/$${build}_*
	rmdir --ignore-fail-on-non-empty commands
build/%.ansi: build/%.map
	./map.py $< > $@
