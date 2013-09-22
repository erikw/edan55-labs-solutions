#!/usr/bin/env python3
# Independent set  lab3 in EDAN55 2013. Generate data.

__author__ = "Erik Westrup, Dmitry Basavin"

import sys
import math

from algorithm import R0, R1, R2
from graph import Graph
from independent_set import read_datafile

data_path = '../data'
#files = {
#R0: ["g{:d}.in".format(x) for x in [4,30,40,50,60]],
#R1: ["g{:d}.in".format(x) for x in [4,30,40,50,60,70,80,90,100]],
#R2: ["g{:d}.in".format(x) for x in [4,30,40,50,60,70,80,90,100,110,120]]
#}

files = {
R0: ["g{:d}.in".format(x) for x in [4,30,]],
R1: ["g{:d}.in".format(x) for x in [4,30,40,50]],
R2: ["g{:d}.in".format(x) for x in [4,30,40,50,60,70]]
}


def run(algorithm, files):
    results = []
    for data_file in files:
        graph = read_datafile("{:s}/{:s}".format(data_path, data_file))
        algorithm.nbr_calls = 0
        algorithm(graph)
        results.append((len(graph.mates),algorithm.nbr_calls))
    return results

def main():
    for algorithm in [R0, R1, R2]:
        results = run(algorithm, files[algorithm])
        print("{:s}:".format(algorithm.__name__))        
        for result in results:
            log_calls = math.log(result[1], 2)
            over_n_calls = math.log(result[1], 2) / result[0]
            print("\tn={:d}, calls={:d}, log2(calls)={:.3f}, log2(calls)/n={:.3f}".format(result[0], result[1], log_calls, over_n_calls))


if __name__ == '__main__':
    sys.exit(main())
