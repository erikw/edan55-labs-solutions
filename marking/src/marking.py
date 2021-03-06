#!/usr/bin/env python3
# Marking lab in EDAN55.

__author__ = "Erik Westrup"
__email__ = "erik.westrup@gmail.com"

import sys
import argparse

from randprocs import *
from intrange import IntRange
from marker import Marker, MarkerR3


def parse_args():
    parser = argparse.ArgumentParser(description="Mark trees according to different random processes.")
    parser.add_argument("-r", "--random-proc", type=IntRange(1, 3), default=1, help="Which random process to use of R[1-3]")
    parser.add_argument("-H", "--tree-height", type=IntRange(1, float("inf")), default=3, help="Height h of the complete bin tree.")
    args = parser.parse_args()
    nbr_nodes = 2**(args.tree_height) - 1
    rand_proc = {
            1 : R1(nbr_nodes),
            2 : R2(nbr_nodes),
            3 : R3(nbr_nodes)
            }[args.random_proc]
    return rand_proc, args.tree_height

def main():
    (rand_proc, tree_height) = parse_args()
    if isinstance(rand_proc, R3):
        marker = MarkerR3(tree_height)
    else:
        marker = Marker(tree_height)
    marker.run(rand_proc)
    print(marker.status())
    return 0


if __name__ == '__main__':
    sys.exit(main())
