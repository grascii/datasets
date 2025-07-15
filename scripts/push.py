"""
Create and push a dataset to HuggingFace
"""

import argparse
import sys

from datasets import load_dataset


argparser = argparse.ArgumentParser()
argparser.add_argument("images", help="path to an image directory")
argparser.add_argument("repo", help="HuggingFace repo to push to")
argparser.add_argument("--revision", "-r", help="branch to push the files to")
argparser.add_argument("--token", "-t", help="HuggingFace authentication token")
args = argparser.parse_args(sys.argv[1:])


dataset = load_dataset("imagefolder", data_dir=args.images)

dataset.push_to_hub(
    args.repo,
    revision=args.revision,
    private=True,
    token=args.token,
)
