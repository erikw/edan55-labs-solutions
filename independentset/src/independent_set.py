#!/usr/bin/env python3
# Independent set  lab3 in EDAN55 2013.

__author__ = "Erik Westrup, Dmitry Basavin"

import sys
import argparse
from os.path import basename

from algorithm import R0, R1, R2
from node import Node
from graph import Graph

def read_datafile(filename):
    try:
        filehandle = open(filename, 'r')
    except IOError:
        print("Could not open file %s.".format(filename))
        sys.exit(2)
    nbr_nodes = int(filehandle.readline())
    
    existing_nodes = {}
    for i in range(nbr_nodes):
        node = get_or_create_node(i, existing_nodes)
        neighbours = [int(x) for x in filehandle.readline().split()]
        for j in range(nbr_nodes):
            if neighbours[j]:
                neighbour_node = get_or_create_node(j, existing_nodes)
                node.add_edge(neighbour_node)
                neighbour_node.add_edge(node)
    filehandle.close()

    graph = Graph([x for x in existing_nodes.values()])
    return graph

def get_or_create_node(i, existing_nodes):
    if i in existing_nodes.keys():
        node = existing_nodes[i]
    else:
        node = Node(i)
        existing_nodes[i] = node
    return node

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
    max_is = algorithm(graph)
    print("The maximum number of independent nodes are {:d}".format(max_is))
    return 0

if __name__ == '__main__':
    sys.exit(main())
