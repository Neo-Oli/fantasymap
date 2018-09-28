define display
	less -RS "$(1)"
endef

.PHONY: whole
whole: build/map
	$(call display,$<)
build/map: map
	./map.py "$<" > "$@"

.PHONY: all
all: build/map html build/yuba

map: build map.py
	@touch "$@"
build:
	mkdir -p build

.PHONY: clean
clean:
	rm -fvr build

.PHONY: yuba
yuba: build/yuba
	$(call display,$<)
build/yuba: map
	./getsubmap.sh map 173 40 762 165 > "$@"

.PHONY: html
html: build/index.html build/map.css
build/index.html: map
	./map.py -x map > "$@"
build/map.css:
	cp map.css build

