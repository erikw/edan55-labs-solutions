#!/usr/bin/env python3
# Independent set  lab3 in EDAN55 2013.

__author__ = "Erik Westrup, Dmitry Basavin"

import sys
import argparse
from os.path import basename

from algorithm import R0, R1, R2
from graph import Graph

def read_datafile(filename):
    try:
        filehandle = open(filename, 'r')
    except IOError:
        print("Could not open file %s.".format(filename))
        sys.exit(2)
    nbr_nodes = int(filehandle.readline())
    graph = Graph(range(nbr_nodes))
    existing_nodes = {}
    for i in range(nbr_nodes):
        neighbours = [int(x) for x in filehandle.readline().split()]
        for j in range(nbr_nodes):
            if neighbours[j]:
                graph.add_edge(i, j)
    filehandle.close()
#    print(graph)
#   graph.new_version()
#    graph.remove_node([graph.nodes[0]])
#    print(graph)
#    graph.rewind_version()
#    print(graph)
#    graph.new_version()
#    graph.remove_node(graph.neighbourhood(graph.nodes[0]))
#    print(graph)
#    graph.rewind_version()
#    print(graph)
    return graph

def parse_args():
    parser = argparse.ArgumentParser(description='Find a maximum independent set')
    parser.add_argument('-a', '--algorithm', choices=['R0', 'R1', 'R2'], action='store', default='R0', help="The algoritm to use.")
    parser.add_argument('filename', nargs='?', default='../data/g4.in', help="File name to read graph from.")
    args = parser.parse_args()

    alg_func = {
            'R0' : R0,
            'R1' : R1,
            'R2' : R2
            }[args.algorithm]
    return args.filename, alg_func

def main():
    filename, algorithm = parse_args()
    graph = read_datafile(filename)
    algorithm.nbr_calls = 0 
    max_is = algorithm(graph)
    print("The maximum number of independent nodes are {:d}\nNumber of calls to {:s} was {:d}\n".format(max_is, algorithm.__name__, algorithm.nbr_calls))
    return 0

if __name__ == '__main__':
    sys.exit(main())
