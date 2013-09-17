import random
import math
import numpy.random
from itertools import chain, combinations, product
import functools

def R(edges, nbr_vertices):
    setA = set()
    # Verticies indexed starting from 1.
    for i in range(1, nbr_vertices + 1):
        flip = random.randint(0,1)
        if flip:
            setA.add(i)
    return calculate_cut_weight(edges, setA)
    

def L(edges, nbr_vertices):
    k = math.ceil(math.log(nbr_vertices + 1, 2))
    b_array = list(random.randint(0,1) for i in range(0,k))
    subsets = chain.from_iterable(combinations(b_array, n) for n in range(1,k + 1))
    setA = set()
    i = 1
    for subset in subsets:
        rs = functools.reduce(lambda x,y: x ^ y, subset)
        if (rs):
            setA.add(i)
        i += 1
        if i > nbr_vertices:
            break
    return calculate_cut_weight(edges, setA)


def Z(edges, nbr_vertices):
    k = math.ceil(math.log(nbr_vertices + 1, 2))
    subsets = []
    for seq in product([0,1], repeat=3):
        subsets.append(list(seq))
    setA = set()
    i = 1
    for subset in subsets:
        print(subset)
        rs = functools.reduce(lambda x,y: x ^ y, subset)
        if (rs):
            setA.add(i)
        i += 1
        if i > nbr_vertices:
            break
    return calculate_cut_weight(edges, setA)

def calculate_cut_weight(edges, setA):
    cut_weight = 0
    for edge in edges:
        if len(setA.intersection({edge.v1, edge.v2})) == 1:
            cut_weight += edge.weight
    return cut_weight
