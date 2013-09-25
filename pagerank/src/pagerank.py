#!/usr/bin/env python3
# Independent set  lab4 in EDAN55 2013.

__author__ = "Erik Westrup, Dmitry Basavin"

import sys
import argparse
import random

ALPHA = 85/100

def read_datafile(filename):
    try:
        filehandle = open(filename, 'r')
    except IOError:
        print("Could not open file %s.".format(filename))
        sys.exit(2)
    nbr_nodes = int(filehandle.readline())
    adj_dict = {}
    for i in range(nbr_nodes):
        adj_dict[i] = list() 
        pairs = [int(x) for x in filehandle.readline().split()]
        for i in range(0, len(pairs), 2):
            a = pairs[i];
            b = pairs[i + 1];
            adj_dict[a].append(b)
    filehandle.close()
    return adj_dict

def parse_args():
    parser = argparse.ArgumentParser(description='Do the google page rank.')
    parser.add_argument('-n', '--nbr-iterations', type=int, required=True, help='Number of iterations.')
    parser.add_argument('filename', nargs='?', default='../data/three.txt', help="File name to read graph from.")
    args = parser.parse_args()

    return args.nbr_iterations, args.filename


def page_rank(adj_dict, nbr_iterations):
    cur_node = 0
    freqs = {x:0 for x in range(len(adj_dict))} # nodeid -> visit frequency
    for itr in range(nbr_iterations):
        freqs[cur_node] +=1
        flip = random.random()
        if flip <= ALPHA and adj_dict[cur_node]:
            cur_node = random.choice(adj_dict[cur_node])        
        else:
            nodes = list(range(len(adj_dict)))
            nodes.remove(cur_node)
            cur_node = random.choice(nodes)
    for node in freqs.keys():
        freqs[node] /= nbr_iterations
    return freqs

def main():
    nbr_iterations, filename = parse_args()
    adj_dict = read_datafile(filename) # nodeid -> set(nodeids)
    rel_freqs = page_rank(adj_dict, nbr_iterations)
    print(rel_freqs)
    return 0

if __name__ == '__main__':
    sys.exit(main())
