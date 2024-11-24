"""
Build a dictionary with normalized grascii forms
"""
import argparse
import sys
from pathlib import Path

from grascii import DictionaryBuilder
from grascii.dictionary.build import DictionaryOutputOptions
from grascii.dictionary.pipeline import standardize_case, CancelPipeline
from grascii.parser import GrasciiParser
from grascii.similarities import get_node

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "infiles", nargs="+", type=Path, help="the dictionary source files"
)
argparser.add_argument(
    "output", type=Path, help="output directory"
)
args = argparser.parse_args(sys.argv[1:])


parser = GrasciiParser()


def parse(grascii, translation, logger):
    try:
        interpretation = next(parser.interpret(grascii))
    except Exception:
        raise CancelPipeline()
    # filter out annotations
    filtered = filter(lambda x: not isinstance(x, list), interpretation)
    # Use a singular representation for all strokes and join them with '-'
    # Ex. TD, DT, and DT are all mapped to TD
    normalized = "-".join(map(lambda s: get_node(s)[0], filtered))
    return normalized, translation


builder = DictionaryBuilder(
    pipeline=[standardize_case, parse]
)

builder.build(
    infiles=args.infiles,
    output=DictionaryOutputOptions(args.output)
)
