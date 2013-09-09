#!/usr/bin/env python3
# Generate test data from samples of marking usiing different combinations of R[123] and H.

# TODO calc mean, stddev etc
# TODO collect all data in a matrix or such

import sys

import numpy

from randprocs import *
from marker import *

samples = 2**4
max_tree_height = 8 + 1 # TODO kaputt

def print_log(text, indent=1):
    print('-' * indent + "> {:s}".format(text))

def main():
    stats = [[None] * 4 for i in range(0, max_tree_height)]
    for tree_height in range(2, max_tree_height):
        nbr_nodes = 2**tree_height - 1
        #print_log("height = {:d}, N = {:d}".format(tree_height, nbr_nodes), 1)
        proc_num = 1
        for rand_proc in (R1(nbr_nodes), R2(nbr_nodes), R3(nbr_nodes)):
            #print_log("Using random process {:s}".format(rand_proc.name), 4)
            nbr_rounds = []
            for sample in range(0, samples):
                #print_log("Sample number {:d}".format(sample), 8)
                if proc_num == 3:
                    marker = MarkerR3(tree_height)
                else:
                    if proc_num == 2:
                        rand_proc = R2(nbr_nodes)
                    marker = Marker(tree_height)
                marker.run(rand_proc)
                #print(marker.status())
                nbr_rounds.append(marker.mark_count)
            #print(numpy.mean(nbr_rounds))
            stats[tree_height][proc_num] = {}
            stats[tree_height][proc_num]['mean_rounds'] = numpy.mean(nbr_rounds)
            #stats[tree_height][proc_num - 1]['std_dev_rounds'] = 
            proc_num += 1


    # TODO print latex tabel instread to file
    #print("H | N      | R1              | R2               | R3")
    #print('  |' + (' ' * 10) + ("mRnds | mTime   |  " * 3))
    #print('-' * 66)
    #for height in range(2, max_tree_height):
        #print("{:d} | {:4d}| ".format(height, (2**height - 1)), end='')
        #for proc_num in (1,2,3):
            #print("{:.1f}   {:.8f}     | ".format(stats[height][proc_num]['mean_rounds'], stats[height][proc_num]['mean_time']), end='')
        #print()

    #print(stats)

    return 0

if __name__ == "__main__":
    sys.exit(main())
