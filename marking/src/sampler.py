#!/usr/bin/env python3
# Generate test data from samples of marking usiing different combinations of R[123] and H.

# TODO min number send count in R3 deterministic?
# TODO is algo linear in time?
# TODO  which is the last number alice sends
# TODO R1 for H=14 should be more like 35000 +- stddev 8000
# TODO for R1,N=3 I only get close to Thores values if i sample ~ 100 times, why?

__author__ = "Erik Westrup"
__email__ = "erik.westrup@gmail.com"

import sys
import re

import numpy

from randprocs import *
from marker import *

samples = 10
max_tree_height = 20

matrix_file_name = '../docs/myreport/data_table.tex'
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


def collect_samples():
    data = [[None] * 4 for i in range(0, max_tree_height + 1)]
    for tree_height in range(2, max_tree_height + 1):
        nbr_nodes = 2**tree_height - 1
        proc_num = 1
        for rand_proc in (R1(nbr_nodes), R2(nbr_nodes), R3(nbr_nodes)):
            nbr_rounds = []
            for sample in range(0, samples):
                if proc_num == 3:
                    marker = MarkerR3(tree_height)
                else:
                    if proc_num == 2:
                        rand_proc = R2(nbr_nodes)
                    marker = Marker(tree_height)
                marker.run(rand_proc)
                nbr_rounds.append(marker.mark_count)
            data[tree_height][proc_num] = {}
            data[tree_height][proc_num]['rounds_stddev'] = numpy.std(nbr_rounds)
            data[tree_height][proc_num]['rounds_mean'] = numpy.mean(nbr_rounds)
            proc_num += 1
    return data

def sci_format(stddev, mean):
    stddev = "{:.1e}".format(stddev)
    stddev, sign, exp = re.split("e(\+|-)", stddev)
    exp = int(exp)
    if exp > 0:
        if sign == '+': 
            mean /= (10 ** exp)
        else:
            mean *= (10 ** exp)
    outstr = " & ${:.1f} \pm {:s}$".format(mean, stddev)
    if exp > 0:
        if exp == 1 and sign != '-':
            outstr += " $\\times 10$"
        else:
            if sign == '+':
                outstr += " $\\times 10^{{{:d}}}$".format(exp)
            else:
                outstr += " $\\times 10^{{{:s}{:d}}}$".format(sign, exp)
    return outstr

def gen_latex_file(data):
    matrix_file = open(matrix_file_name, 'w')
    matrix_file.write(latex_matrix_header)
    for height in range(2, max_tree_height + 1):
        matrix_file.write("{:d} & {:d} ".format(height, (2**height - 1)))
        for proc_num in (1,2,3):
            fmtnbr = sci_format(
                    data[height][proc_num]['rounds_stddev'],
                    data[height][proc_num]['rounds_mean']
                    )
            matrix_file.write(fmtnbr)
        matrix_file.write(" \\\\\n")
    matrix_file.write(latex_matrix_footer + "\n")

def main():
    data = collect_samples()
    gen_latex_file(data)
    return 0

if __name__ == "__main__":
    sys.exit(main())
