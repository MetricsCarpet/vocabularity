#!/usr/bin/env python
import os
import argparse
from vocabularity.grammar_parsing import parseprint


# node = ast.parse(code)
# print ast.dump(node)
# parseprint(code)
# parseprint(open(__file__).read())


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="filename", required=True,
                        help=".py (python source) input file", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()
    print args
