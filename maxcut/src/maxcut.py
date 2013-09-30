#!/usr/bin/env python3
# Maxcut lab2 in EDAN55 2013.

__author__ = "Erik Westrup, Dmitry Basavin"

import sys
import argparse
from os.path import basename

from edge import Edge
from algorithms import R, L, Z

latex_file = "../docs/myreport/r1_data.tex"
no_samples = 100

latex_data_pre = r"""
\begin{tikzpicture}
\begin{axis}[
  height= 5cm,
  ybar interval,
  xmin = 0,  xmax = 13658,
  xtick =       {0   ,   5000,   10000, 13658},
  xticklabels = { $0$, $5000$, $10000$,   OPT},
  x tick label as interval = false,
  scaled ticks = false
]
    \addplot+[hist={bins=101}]
        table[y index=0] {
"""

latex_data_post = r"""
    };
\end{axis}
\end{tikzpicture}
"""

def read_datafile(filename):
    try:
        filehandle = open(filename, 'r')
    except IOError:
        print("Could not open file %s.".format(filename))
        sys.exit(2)
    nbr_vertices, nbr_edges = (int(number) for number in filehandle.readline().split())
    edges = []
    for i in range(0, nbr_edges):
        v1, v2, weight = (int(number) for number in filehandle.readline().split())
        edges.append(Edge(v1, v2, weight))

    filehandle.close()
    return edges, nbr_vertices

def write_latex_file(results):
    file_handle = open(latex_file, 'w')
    file_handle.write(latex_data_pre)
    for result in results:
        file_handle.write("{:d}\n".format(result))
    file_handle.write(latex_data_post)
    file_handle.close()

def set_opt_from_filename(filename):
    if basename(filename) == "matching_1000.txt":
        opt = 500
    elif basename(filename) == 'pw09_100.9.txt':
        opt = 13658
    else:
        raise ValueError("The input file \"{:s}\" is not recognized.".format(filename))
    return opt

def parse_args():
    parser = argparse.ArgumentParser(description='Approximate a max cut.')
    parser.add_argument('-a', '--algorithm', choices=['R', 'L', 'Z'], action='store', default='R', help="The algoritm for appoximation to use.")
    parser.add_argument('filename', nargs='?', default='../data/matching_1000.txt', help="File name to read graph from.")
    args = parser.parse_args()

    alg_func = {
            'R' : R,
            'L' : L,
            'Z' : Z
            }[args.algorithm]
    return args.filename, alg_func

def main():
    filename, algorithm = parse_args()
    opt = set_opt_from_filename(filename)
    edges, nbr_vertices = read_datafile(filename)

    maxcut = 0;
    results = []
    for i in range(0, no_samples):
        candidate = algorithm(edges, nbr_vertices)
        results.append(candidate)
        if candidate > maxcut:
            maxcut = candidate
    print("Over {:d} samples, the found maxcut is {:d}".format(no_samples, maxcut))
    avg_cutsize = sum(results) / len(results)
    print("Average cutsize is {:.2f}".format(avg_cutsize))
    print("which is {:.2f}% of OPT(={:d})".format(avg_cutsize/opt * 100, opt))
    write_latex_file(results)
    return 0

if __name__ == '__main__':
    sys.exit(main())
