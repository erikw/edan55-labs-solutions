#!/usr/bin/env python3
# Generate test data from samples of marking usiing different combinations of R[123] and H.

# TODO measure wall clock time
# TODO calc mean, stddev etc

import sys

from randprocs import *
from marker import *

samples = 2**2
max_tree_height = 4

def print_log(text, indent=1):
    print('-' * indent + "> {:s}".format(text))

def main():
    for tree_height in range(2, max_tree_height):
        print_log("height = {:d}, N = {:d}".format(tree_height, (2**tree_height - 1)), 1)
        for rand_proc in (R1(tree_height), R2(tree_height), R3(tree_height)):
            print_log("Using random process {:s}".format(rand_proc.name), 4)
            for sample in range(0, samples):
                print_log("Sample number {:d}".format(sample), 8)
                if isinstance(rand_proc, R3):
                    marker = MarkerR3(tree_height)
                else:
                    marker = Marker(tree_height)
                marker.run(rand_proc)
                print(marker.status())



    return 0

if __name__ == "__main__":
    sys.exit(main())
