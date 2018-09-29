define display
	less -RS "$(1)"
endef

.PHONY: whole
whole: build/map
	$(call display,$<)
build/map: map map.py
	mkdir -p build
	./map.py "$<" > "$@"

.PHONY: all
all: build/map html build/yuba build/witton build/onyx

.PHONY: clean
clean:
	rm -fvr build


.PHONY: html
html: build/index.html build/map.css
build/index.html: map map.py
	mkdir -p build
	./map.py -x map > "$@"
build/map.css: map.css
	mkdir -p build
	cp map.css build

.PHONY: yuba
yuba: build/yuba
	$(call display,$<)
build/yuba: map map.py
	mkdir -p build
	bash -c './map.py <(./cutmapfile.py map 174 760 217 926 )' > "$@"

.PHONY: witton
witton: build/witton
	$(call display,$<)
build/witton: map map.py
	mkdir -p build
	bash -c './map.py <(./cutmapfile.py map 100 24 135 135)' > "$@"

.PHONY: onyx
onyx: build/onyx
	$(call display,$<)
build/onyx: map map.py
	mkdir -p build
	bash -c './map.py <(./cutmapfile.py map 313 100 345 190)' > "$@"
