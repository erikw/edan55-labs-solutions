#!/usr/bin/env python3

import sys
from random import randint
from edge import Edge

latex_file = "../docs/myreport/r1_data.tex"

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



def main():
    if (len(sys.argv)  != 2):
        print("Expected one argument: file name.")
        return 1
    filename = sys.argv[1]
    if filename == "../data/matching_1000.txt":
        opt = 500
    elif filename == '../data/pw09_100.9.txt':
        opt = 13658
    else:
        raise ValueError("The input file \"{:s}\" is not recognized.".format(filename))
    edges, nbr_vertices = read_datafile(filename)

    maxcut = 0;
    results = []
    for i in range(0, 100):
        candidate = R(edges, nbr_vertices)
        results.append(candidate)
        if candidate > maxcut:
            maxcut = candidate
    print("the found maxcut is {:d}".format(maxcut))
    avg_cutsize = sum(results) / len(results)
    print("average cutsize is {:.2f}".format(avg_cutsize))
    print("which is {:.2f}% of OPT(={:d})".format(avg_cutsize/opt * 100, opt))
    write_latex_file(results)
    return 0

def R(edges, nbr_vertices):
    set0 = set()
    set1 = set()
    for i in range(0, nbr_vertices):
        flip = randint(0,1)
        if not flip:
            set0.add(i)
        else:
            set1.add(i)

    maxcut = 0
    for edge in edges:
        if (edge.v1 in set0 and edge.v2 in set1) or (edge.v1 in set1 and edge.v2 in set0):
            maxcut += edge.weight

    return maxcut

if __name__ == '__main__':
    sys.exit(main())
