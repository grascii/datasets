"""
Create a metadata.csv for a set of images
"""

import argparse
import csv
import glob
import sys
from pathlib import Path

from grascii.dictionary import Dictionary


argparser = argparse.ArgumentParser()
argparser.add_argument("images", type=Path, help="path to an image directory")
argparser.add_argument(
    "dictionary", type=Path, help="path to a normalized grascii dictionary"
)
args = argparser.parse_args(sys.argv[1:])


# dump all entries
entries = Dictionary.new(args.dictionary).dump()

# map translations to entries
to_grascii = {}
for entry in entries:
    key = entry.translation.lower().strip(".")
    if key in to_grascii:
        print("Duplicate key:", key)
    to_grascii[key] = entry

# create metadata.csv
base_path = args.images.joinpath("train")
with Path(base_path, "metadata.csv").open("w", newline="\n") as csv_file:
    field_names = ["file_name", "grascii_normalized", "longhand"]
    writer = csv.DictWriter(csv_file, fieldnames=field_names, dialect="unix")
    writer.writeheader()

    for pathname in sorted(glob.glob(f"{base_path}/[a-z]/*.png")):
        path = Path(pathname)
        word = path.stem

        try:
            key = word.lower().strip(".")
            entry = to_grascii[key]
            writer.writerow(
                {
                    "file_name": path.relative_to(base_path),
                    "grascii_normalized": entry.grascii,
                    "longhand": entry.translation,
                }
            )
            del to_grascii[key]
        except KeyError:
            print("no entry for:", word)
