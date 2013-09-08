#!/usr/bin/env python3
# Marking lab in EDAN55.

__author__ = "Erik Westrup"
__email__ = "erik.westrup@gmail.com"

import sys
import argparse

from randprocs import *
from intrange import IntRange
from marker import Marker


def parse_args():
    parser = argparse.ArgumentParser(description="Mark trees according to different random processes.")
    parser.add_argument("-r", "--random-proc", type=IntRange(1, 3), default=1, help="Which random process to use of R[1-3]")
    parser.add_argument("-H", "--tree-height", type=IntRange(1, float("inf")), default=3, help="Height h of the complete bin tree.")
    args = parser.parse_args()
    rand_proc = {
            1 : R1(),
            2 : R2(),
            3 : R3()
            }[args.random_proc]
    return rand_proc, (args.tree_height - 1)

def main():
    (rand_proc, tree_height) = parse_args()
    marker = Marker(tree_height)
    while not marker.all_marked():
        nbr = rand_proc.next_nbr(marker)
        print("{:d}\t->\tSent by Alice.".format(nbr))
        marker.mark(nbr)
    print(marker.status())
    #print("All done.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
