define display
	less -RS "$(1)"
endef

REQ := map.py map.map Makefile legend.map map.css
.PHONY: whole
whole: build/map
	$(call display,$<)
build/map: $(REQ)
	mkdir -p build
	./map.py map.map > "$@"
.PHONY: edit
edit: build/vimrc
	$(EDITOR) map.map -c ":so build/vimrc"
build/vimrc: map.py
	mkdir -p build
	./map.py -V /dev/null > "$@"

.PHONY: all
all:\
	test\
	build/vimrc\
	build/map\
	build/index.html\
	build/help.html\
	build/monochrome\
	build/monochrome.html\
	build/legend\
	build/yuba\
	build/witton\
	build/onyx\
	build/angilles\


.PHONY: clean
clean:
	rm -fvr build

.PHONY: help
help: build/legend
	$(call display,$<)
build/legend: $(REQ)
	./map.py legend.map > "$@"

.PHONY: test
test: build/test_legend build/test_map
build/test_legend: $(REQ)
	mkdir -p build
	./map.py -v legend.map
	@touch "$@"
build/test_map: $(REQ)
	mkdir -p build
	./map.py -v map.map
	@touch "$@"
.PHONY: html
html: build/index.html
build/index.html: $(REQ)
	mkdir -p build
	./map.py -x map.map > "$@"

build/help.html: $(REQ)
	./map.py -x legend.map > "$@"

.PHONY: monochrome
monochrome: build/monochrome
	$(call display,$<)
build/monochrome: $(REQ)
	mkdir -p build
	./map.py -b map.map > "$@"

.PHONY: monochrome-html
monochrome-html: build/monochrome.html
build/monochrome.html: $(REQ)
	mkdir -p build
	./map.py -xb map.map > "$@"

.PHONY: yuba
yuba: build/yuba
	$(call display,$<)
build/yuba: $(REQ)
	mkdir -p build
	bash -c './map.py <(./cutmapfile.py map.map 170 760 217 926 )' > "$@"

.PHONY: witton
witton: build/witton
	$(call display,$<)
build/witton: $(REQ)
	mkdir -p build
	bash -c './map.py <(./cutmapfile.py map.map 100 24 135 135)' > "$@"

.PHONY: onyx
onyx: build/onyx
	$(call display,$<)
build/onyx: $(REQ)
	mkdir -p build
	bash -c './map.py <(./cutmapfile.py map.map 319 120 340 170)' > "$@"

.PHONY: angilles
angilles: build/angilles
	$(call display,$<)
build/angilles: $(REQ)
	mkdir -p build
	bash -c './map.py <(./cutmapfile.py map.map 17 711 108 836)' > "$@"
