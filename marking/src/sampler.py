#!/usr/bin/env python3
# Generate test data from samples of marking usiing different combinations of R[123] and H.

# TODO calc mean, stddev etc
# TODO collect all data in a matrix or such

import sys
import re

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
                nbr_rounds.append(marker.mark_count)
            stats[tree_height][proc_num] = {}
            stats[tree_height][proc_num]['rounds_stddev'] = numpy.std(nbr_rounds)
            stats[tree_height][proc_num]['rounds_mean'] = numpy.mean(nbr_rounds)
            proc_num += 1

    matrix_file = open(matrix_file_name, 'w')
    matrix_file.write(latex_matrix_header)
    for height in range(2, max_tree_height):
        matrix_file.write("{:d} ".format(2**height - 1))
        for proc_num in (1,2,3):
            stddev = stats[height][proc_num]['rounds_stddev']
            stddev = "{:.1e}".format(stddev)
            #stddev, exp = stddev.split("e(+|-)", 1)
            stddev, sign, exp = re.split("e(\+|-)", stddev)
            if sign == '+': 
                sign = ''
            exp = int(exp)
            mean = stats[height][proc_num]['rounds_mean']
            if exp == 0:
                matrix_file.write(" & {:f} \pm {:s}".format( mean, stddev))
            else:
                matrix_file.write(" & {:f} \pm {:s} x $10^{{{:s}{:d}}}$".format( mean, stddev, sign, exp))
        matrix_file.write(" \\\\\n")
    matrix_file.write(latex_matrix_footer + "\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
