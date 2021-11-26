import argparse
import importlib
import os

from . import utils

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="Path to folder containing .git folder")
parser.add_argument("action", type=str, choices=["a", "tree", "blob", "tag", "commit"], help="Type of git object")
parser.add_argument('obj', nargs='?', default="")
parser.add_argument("-l", "--list", action='store_true')

def main(args):
    os.chdir(args.path)

    if args.obj:
        args.obj = utils.autofind(args.obj)

    return importlib.import_module(f".actions.{args.action}", package="gitfsls").command(args)


if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    code = main(args)
    exit(code)
