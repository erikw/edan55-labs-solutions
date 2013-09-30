#!/usr/bin/env python3
# Independent set  lab4 in EDAN55 2013.

__author__ = "Erik Westrup, Dmitry Basavin"

import sys
import argparse
import random
import math
import operator
import copy

import numpy
import scipy.sparse

from matrices import *


def read_datafile(filename):
    try:
        filehandle = open(filename, 'r')
    except IOError:
        print("Could not open file %s.".format(filename))
        sys.exit(2)
    nbr_nodes = int(filehandle.readline())
    adj_dict = {x:[] for x in range(nbr_nodes)}
    for i in range(nbr_nodes):
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
    parser.add_argument('-m', '--method', type=int, choices=[1,11,2,3], default=1, help="What method to use.")    
    args = parser.parse_args()

    if args.method == 2 and not power_of_two(args.nbr_iterations):
        print("The numbe of iterations for the second method should be a pwoer of 2")            
        sys.exit(2)
    return args.nbr_iterations, args.filename, args.method

def power_of_two(number):
    return math.log(number,2).is_integer()


def page_rank(adj_dict, nbr_iterations):
    cur_node = 0
    freqs = {x:0 for x in range(len(adj_dict))} # nodeid -> visit frequency
    for itr in range(nbr_iterations):
        freqs[cur_node] +=1
        cur_node = next_node(adj_dict, cur_node)
    for node in freqs.keys():
        freqs[node] /= nbr_iterations
    return freqs


def page_rank_stable(adj_dict, nbr_iterations):
    cur_node = 0
    freqs = {x:0 for x in range(len(adj_dict))} # nodeid -> visit frequency
    freqs[cur_node] +=1
    count = 1
    unstable = True
    while unstable:
        cur_node = next_node(adj_dict, cur_node)
        prev_freqs = copy.deepcopy(freqs)
        freqs[cur_node] +=1
        count +=1
        unstable = is_unstable(freqs, prev_freqs, count)
        #for node in freqs.keys():
        #    print("{:d} ({:f}\%)  &".format(node, freqs[node] / count), end='')  
        #print("")
    for node in freqs.keys():
        freqs[node] /= count
    return freqs, count

def is_unstable(freqs, prev_freqs, count):
    for node in freqs.keys():
        # use 3 decimal places to determine stability
        cur = int(freqs[node]/count * 1000)
        prev = int(prev_freqs[node]/(count-1) * 1000)
        if not cur == prev:
            return True
    return False
    
def next_node(adj_dict, cur_node):
    flip = random.random()
    if flip <= ALPHA and adj_dict[cur_node]:
        next_node = random.choice(adj_dict[cur_node])        
    else:
        nodes = list(range(len(adj_dict)))
        next_node = random.choice(nodes)
    return next_node
    
def q_iterations(adj_dict, nbr_iterations):
    Q = build_matrix(adj_dict)
    p_to_the(Q, 10)
    p = numpy.array([1] + [0 for x in range(len(adj_dict) - 1)])
    r = math.log(nbr_iterations, 2)
    for i in range(int(r)):
        Q *= Q
    final_distribution = p*Q
    return {i:final_distribution[0,i] for i in range(len(adj_dict))}

def p_to_the(P, number):
    Po = P.copy()
    for i in range(number - 1):
        Po *= P
    print(Po) 

def dh_iterations(adj_dict, nbr_iterations):
    H, D  = build_static_matrices(adj_dict)
    #H, D, Do = build_static_matrices(adj_dict)

    # Formular verification.
    #num_nodes = len(adj_dict)
    #p = numpy.array([1] + [0 for x in range(num_nodes - 1)])
    #P = build_matrix(adj_dict)
    #ones = numpy.mat(numpy.ones(shape=(len(adj_dict),len(adj_dict))))
    #Ptest  = ALPHA * (H + Do) + ((1-ALPHA)/len(adj_dict)) * p * ones
    #print(P)
    #print(Ptest)

    #print(H)
    #print(D)


    num_nodes = len(adj_dict)
    p = numpy.array([1] + [0 for x in range(num_nodes - 1)])
	
    for i in range(nbr_iterations):
        alpha_p = ALPHA * p
        p1_elem = (1-ALPHA) * sum(p) / num_nodes
        p1 = numpy.array([ p1_elem for i in range(num_nodes)])
        p = alpha_p * H + mul_vector_matrix(alpha_p, D) + p1
		
    return {i : p[i] for i in range(len(adj_dict))}

def print_freqs(freqs, method):
    print("Method #{:d}\nNode\tRelFreq".format(method))
    for node in freqs.keys():
        print("{:d}\t{:f}".format(node, freqs[node]))

def most_frequent(freqs, number):
    return sorted(freqs.items(), key=operator.itemgetter(1), reverse=True)[0:number]

def main():
    nbr_iterations, filename, method = parse_args()
    adj_dict = read_datafile(filename) # nodeid -> list(nodeids)
    if method is 1:
        rel_freqs = page_rank(adj_dict, nbr_iterations)
    elif method is 11:
        rel_freqs, count = page_rank_stable(adj_dict, nbr_iterations)
        print("Count is {:d}".format(count))
    elif method is 2:
        rel_freqs = q_iterations(adj_dict, nbr_iterations)
    elif method is 3:    
        rel_freqs = dh_iterations(adj_dict, nbr_iterations)    
    print_freqs(rel_freqs, method)

    most_freq = most_frequent(rel_freqs, 5)
    for node, freq in most_freq:
        print("{:d} ({:f}\%)  &".format(node, freq * 100), end='')   

    print("")
    return 0

if __name__ == '__main__':
    sys.exit(main())
