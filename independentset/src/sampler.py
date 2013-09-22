#!/usr/bin/env python3
# Independent set  lab3 in EDAN55 2013. Generate data.

__author__ = "Erik Westrup, Dmitry Basavin"

import sys
import math

from algorithm import R0, R1, R2
from graph import Graph
from independent_set import read_datafile

data_path = '../data'
files = {
R0: ["g{:d}.in".format(x) for x in [4,30,40,50,60]],
R1: ["g{:d}.in".format(x) for x in [4,30,40,50,60,70,80,90,100]],
R2: ["g{:d}.in".format(x) for x in [4,30,40,50,60,70,80,90,100,110,120]]
}

#files = {
#R0: ["g{:d}.in".format(x) for x in [4,30,]],
#R1: ["g{:d}.in".format(x) for x in [4,30,40,50]],
#R2: ["g{:d}.in".format(x) for x in [4,30,40,50,60,70]]
#}

latex_0 = r"""
\begin{tikzpicture}
\begin{axis}[
  height= 5cm,
  xlabel=$n$,
  ylabel={log recursive calls},
  xmin = 20,  xmax = 150,
  xtick =       {20,40,60,80,100,120},
  xticklabels = { $20$, $40$, $60$, $80$, $100$, $120$},
  x tick label as interval = false,
  scaled ticks = false
]
    \addplot[color=black, mark=x] 
	coordinates {
"""

latex_1 = r"""
};
    \addlegendentry{R0}

    \addplot[color=black, mark=o] 
	coordinates {
"""

latex_2 = r"""
};
    \addlegendentry{R1}

    \addplot[color=black, mark=*] 
	coordinates {
"""

latex_3 = r"""
};
    \addlegendentry{R2}
\end{axis}
\end{tikzpicture}
"""


def run(algorithm, files):
    results = {'nbr_calls' : list()}
    for data_file in files:
        graph = read_datafile("{:s}/{:s}".format(data_path, data_file))
        algorithm.nbr_calls = 0
        algorithm(graph)
        results['nbr_calls'].append((len(graph.mates), algorithm.nbr_calls))
    return results

def print_latex_file(results):
    res_file = open("../docs/myreport/output.data", 'w')
    res_file.write(latex_0)
    for size, log_calls in results[0]['log_calls']:
        res_file.write("\t({:d}, {:f})\n".format(size, log_calls)) 
    res_file.write(latex_1)
    for size, log_calls in results[1]['log_calls']:
        res_file.write("\t({:d}, {:f})\n".format(size, log_calls)) 
    res_file.write(latex_2)
    for size, log_calls in results[2]['log_calls']:
        res_file.write("\t({:d}, {:f})\n".format(size, log_calls)) 
    res_file.write(latex_3)


    res_file.close()

def main():
    results = []
    for algorithm in [R0, R1, R2]:
        results.append(run(algorithm, files[algorithm]))
        results[-1]['log_calls'] = list()
        #results[-1]['over_n_calls'] = list()
        for size, nbr_calls in results[-1]['nbr_calls']:
            results[-1]['log_calls'].append((size, math.log(nbr_calls, 2)))
            #results[-1]['over_n_calls'].append(math.log(result[1], 2) / result[0])
    #print_latex_file(results)
    print(results)

if __name__ == '__main__':
    sys.exit(main())
