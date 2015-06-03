#!/usr/bin/env python
import os
import argparse
from vocabularity.grammar_parsing import parseprint


# node = ast.parse(code)
# print ast.dump(node)

# parseprint(code)
parseprint(open(__file__).read())
