from random import randint

def R(edges, nbr_vertices):
    setA = set()
    # In the input file, the vertices are numbered starting from 1.
    for i in range(1, nbr_vertices + 1):
        flip = randint(0,1)
        if flip:
            setA.add(i)

    cut_weight = 0
    for edge in edges:
        # if only one of the endpoints is in setA, then use the edge for maxcut
        if len(setA.intersection({edge.v1, edge.v2})) == 1:
            cut_weight += edge.weight
    return cut_weight

def L(edges, nbr_vertices):
    pass

def Z(edges, nbr_vertices):
    pass

