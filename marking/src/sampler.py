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
\begin{table}
\begin{center}
\begin{tabular}{r | r | r | r | r}
$H$ & $N$ & $R_1$ & $R_2$ & $R_3$ \\ \hline
"""
latex_matrix_footer  = r"""
\end{tabular}
\end{center}
\end{table}
"""


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
        matrix_file.write("{:d} & {:d} ".format(height, (2**height - 1)))
        for proc_num in (1,2,3):
            stddev = stats[height][proc_num]['rounds_stddev']
            stddev = "{:.1e}".format(stddev)
            stddev, sign, exp = re.split("e(\+|-)", stddev)
            exp = int(exp)
            mean = stats[height][proc_num]['rounds_mean']
            outstr = " & ${:.1f} \pm {:s}$".format(mean, stddev)
            if exp > 0:
                if sign == '+': 
                    sign = ''
                    mean /= (10 * exp)
                else:
                    mean *= (10 * exp)
                if exp == 1 and sign != '-':
                    outstr += " $\\times 10$"
                else:
                    outstr += " $\\times 10^{{{:s}{:d}}}$".format(sign, exp)
            matrix_file.write(outstr)
        matrix_file.write(" \\\\\n")
    matrix_file.write(latex_matrix_footer + "\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
