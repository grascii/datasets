"""
Create a metadata.csv for a set of images
"""
import argparse
import csv
import glob
import sys
from pathlib import Path

from grascii import RegexSearcher


argparser = argparse.ArgumentParser()
argparser.add_argument(
    "images", type=Path, help="path to an image directory"
)
argparser.add_argument(
    "dictionary", type=Path, help="path to a normalized grascii dictionary"
)
args = argparser.parse_args(sys.argv[1:])


# dump all entries
searcher = RegexSearcher(dictionaries=[args.dictionary])
results = searcher.search(regexp=r".*")

# map translations to results
to_grascii = {}
for result in results:
    to_grascii[result.entry.translation.lower().strip(".")] = result.entry

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
            writer.writerow({
                "file_name": path.relative_to(base_path),
                "grascii_normalized": entry.grascii,
                "longhand": entry.translation,
            })
            del to_grascii[key]
        except KeyError:
            print("no result for:", word)
