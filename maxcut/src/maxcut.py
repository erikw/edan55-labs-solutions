#!/usr/bin/env python3

import sys
from edge import Edge


def read_datafile(filename):
    try:
        filehandle = open(filename, 'r')
    except IOError:
        print("Could not open file %s.".format(filename))
        sys.exit(2)
    nbr_verticies, nbr_edges = (int(number) for number in filehandle.readline().split())
    #print("{:d}, {:d}".format(nbr_verticies, nbr_edges))
    edges = []
    for i in range(0, nbr_edges):
        v1, v2, weight = (int(number) for number in filehandle.readline().split())
        edges.append(Edge(v1, v2, weight))

    filehandle.close()
    return edges

def main():
    if (len(sys.argv)  != 2):
        print("Expected one argument: file name.")
        return 1
    filename = sys.argv[1]
    edges = read_datafile(filename)

    for edge in edges:
        print(edge)
    return 0

if __name__ == '__main__':
    sys.exit(main())
