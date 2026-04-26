datasets = grascii/gregg-preanniversary-words grascii/gregg-preanniversary-phrases grascii/gregg-anniversary-words

all: $(datasets)

clean:
	rm -rf images/*/*/metadata.jsonl normalized

.PHONY: all clean $(datasets)

gregg-preanniversary-words-dictionary = dictionaries/builtins/preanniversary
gregg-preanniversary-phrases-dictionary = dictionaries/builtins/preanniversary-phrases
gregg-anniversary-words-dictionary = dictionaries/builtins/anniversary

$(datasets): grascii/%: images/%/train/metadata.jsonl scripts/push.py
	python scripts/push.py images/$* $@ --token $(HF_TOKEN)

.SECONDEXPANSION:
images/%/train/metadata.jsonl: normalized/$$($$*-dictionary) images/%/train/[a-z] scripts/metadata.py
	python scripts/metadata.py images/$* normalized/$($*-dictionary)

normalized/%: %/*.txt scripts/dictionary.py
	python scripts/dictionary.py $*/*.txt $@

.NOTINTERMEDIATE: normalized/%
