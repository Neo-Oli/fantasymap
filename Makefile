define display
	less -RS "$(1)"
endef

REQ := map.py map Makefile legend
.PHONY: whole
whole: build/map
	$(call display,$<)
build/map: $(REQ)
	./map.py map > "$@"

.PHONY: all
all: build/map html build/monochrome build/legend build/yuba build/witton build/onyx

.PHONY: clean
clean:
	rm -fvr build/*

.PHONY: help
help: build/legend
	$(call display,$<)
build/legend: $(REQ)
	./map.py legend > "$@"

.PHONY: monochrome
monochrome: build/monochrome
	$(call display,$<)
build/monochrome: $(REQ)
	./map.py -b map > "$@"

.PHONY: html
html: build/index.html build/map.css
build/index.html: $(REQ)
	./map.py -x map > "$@"
build/map.css: map.css
	cp map.css build

.PHONY: yuba
yuba: build/yuba
	$(call display,$<)
build/yuba: $(REQ)
	bash -c './map.py <(./cutmapfile.py map 174 760 217 926 )' > "$@"

.PHONY: witton
witton: build/witton
	$(call display,$<)
build/witton: $(REQ)
	bash -c './map.py <(./cutmapfile.py map 100 24 135 135)' > "$@"

.PHONY: onyx
onyx: build/onyx
	$(call display,$<)
build/onyx: $(REQ)
	bash -c './map.py <(./cutmapfile.py map 319 120 340 170)' > "$@"
