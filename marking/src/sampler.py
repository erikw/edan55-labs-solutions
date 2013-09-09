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

matrix_file_name = '../docs/myreport/stats_table.tex'
latex_matrix_header  = r"""
\medskip\noindent
\begin{tabular}{
    S[table-format = 7]
    S[table-format = 1.1(1)e1]
    S[table-format = 1.1(1)e1]
    S[table-format = 1.1(1)e1]
  } 
% WARNING: This table the (brilliant) siunitx package.
% This allows typesetting of nicely aligned numbers.
% If this is too much to absorb, just use a normal Latex table.
% (Or do the table in another tool, export as PDF, and include it.)
% Or do the whole report in your favourite word processor instead.
\toprule
{ $N$ } & { $R_1$ } & {$R_2$} & {$R_3$} \\\midrule
"""
latex_matrix_footer  = "\end{tabular}"


#def print_log(text, indent=1):
    #print('-' * indent + "> {:s}".format(text))

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
            # TOOD format mean stddev as Thore wants
            stats[tree_height][proc_num]['rounds_mean'] = numpy.mean(nbr_rounds)
            stats[tree_height][proc_num]['rounds_stddev'] = numpy.std(nbr_rounds)
            proc_num += 1


    matrix_file = open(matrix_file_name, 'w')
    matrix_file.write(latex_matrix_header)
    for height in range(2, max_tree_height):
        matrix_file.write("{:d} ".format(2**height - 1))
        for proc_num in (1,2,3):
            matrix_file.write(\
            " & {:f} \pm {:f}".format(\
                    stats[height][proc_num]['rounds_mean'],\
                    stats[height][proc_num]['rounds_stddev']\
                    )
                )
        matrix_file.write(" \\\\\n")
                              
    matrix_file.write(latex_matrix_footer + "\n")



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
