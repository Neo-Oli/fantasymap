define display
	less -RS "$(1)"
endef

.PHONY: whole
whole: build/map
	$(call display,$<)
build/map: map map.py
	./map.py "$<" > "$@"

map: build
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
