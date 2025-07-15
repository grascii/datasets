# Gregg Shorthand Datasets

This repository contains the source images and build scripts for grascii's Gregg Shorthand datasets on
[HuggingFace](https://huggingface.co/collections/grascii/gregg-shorthand-datasets-674bac1d70c47ec921059e6b).

## Datasets

### [gregg-preanniversary-words](https://huggingface.co/datasets/grascii/gregg-preanniversary-words)

This dataset consists of images of shorthand forms from the 1916 *Gregg Shorthand Dictionary*[^1].
Most of the images originated from the [Gregg1916](https://github.com/anonimously/Gregg1916-Recognition)
dataset.

#### Contribution Notes

Images are taken from a scan of the dictionary at 175% zoom.

### [gregg-preanniversary-phrases](https://huggingface.co/datasets/grascii/gregg-preanniversary-phrases)

This Grascii original dataset consists of images of shorthand forms from the 1924 *Gregg Shorthand Phrase Book*[^2].

## Contributing

Contributions are welcome!

### Dataset Quality

If you notice an incorrect or low-quality element in the dataset, please open
an issue to report the problem and/or open a pull request that resolves the
issue. Problematic elements include but are not limited to:

 - misnamed images
   - a name does not match the word represented by an image
   - a name is misspelled
 - poorly cropped images
   - the shorthand form in the image is cut off
   - excessive white-space exists around the shorthand form
 - images with stray marks (such marks should be whited-out)
   - the image contains scan artifacts
   - the image contains parts of adjacent shorthand forms or text

If you notice an error in the Grascii form for an image, open an issue in
the [dictionaries](https://github.com/grascii/dictionaries) repository instead.

[^1]: Gregg, John Robert. Gregg Shorthand Dictionary. Gregg Publishing Company, 1916.
[^2]: Gregg, John Robert. Gregg Shorthand Phrase Book. Gregg Publishing Company, 1924.
