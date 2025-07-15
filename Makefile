datasets = grascii/gregg-preanniversary-words grascii/gregg-preanniversary-phrases

all: $(datasets)

clean:
	rm -rf images/*/*/metadata.csv normalized

.PHONY: all clean $(datasets)

gregg-preanniversary-words-dictionary = dictionaries/builtins/preanniversary
gregg-preanniversary-phrases-dictionary = dictionaries/builtins/preanniversary-phrases

$(datasets): grascii/%: images/%/train/metadata.csv scripts/push.py
	python scripts/push.py images/$* $@ --token $(HF_TOKEN)

.SECONDEXPANSION:
images/%/train/metadata.csv: normalized/$$($$*-dictionary) images/%/train/[a-z] scripts/metadata.py
	python scripts/metadata.py images/$* normalized/$($*-dictionary)

normalized/%: %/*.txt scripts/dictionary.py
	python scripts/dictionary.py $*/*.txt $@

.NOTINTERMEDIATE: normalized/%
