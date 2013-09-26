import sys
import argparse
import random
import math
import operator



import numpy
import scipy.sparse

def build_matrix(adj_dict):
    P = numpy.mat(numpy.zeros(shape=(len(adj_dict),len(adj_dict))))

    for node in adj_dict.keys():
        for mate in adj_dict[node]:
            P[node, mate] += ALPHA/len(adj_dict[node])
        if len(adj_dict[node]) == 0:
            remain_prob = 1
        else:
            remain_prob = (1-ALPHA)
        for other_node in range(len(adj_dict)):
            P[node, other_node] += remain_prob/(len(adj_dict) - 0)
    return P



def build_static_matrices(adj_dict):
    num_nodes = len(adj_dict)
    H =  scipy.sparse.lil_matrix((num_nodes, num_nodes))
    for node in adj_dict.keys():
        deg = len(adj_dict[node])
        for neighbour in adj_dict[node]:
            H[node, neighbour] += 1/deg
    Do = scipy.sparse.lil_matrix((num_nodes, num_nodes))
    D = [0 for x in range(num_nodes)]  

    for node in adj_dict.keys():
        deg = len(adj_dict[node])
        if deg == 0:
            D[node] = 1/num_nodes
            for neighbour in range(len(adj_dict)):            
                Do[node, neighbour] = 1/num_nodes
    return H,D,Do
	

	
def mul_vector_matrix(vector, M):
    val = sum([a*b for a,b in zip(vector, M)])
    res = numpy.array([val for x in range(len(M))])
    return res
