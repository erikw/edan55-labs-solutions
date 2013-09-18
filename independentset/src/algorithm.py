import copy

#counts = [0, 0, 0]
#def count_calls(count_index):
#   def counter(alg_func, *args):
#        counts[count_index] += 1
#        alg_func(args)
#    return counter

def debug(text, depth):
    pass
    #print("{:s}{:s}".format('\t' * depth, text))
     
def contains_unconnected_node(nodes):
    for node in nodes:
        if len(node.neighbours) == 0:
            return node
    return None

def maximum_degree(nodes):
    max_deg = 0
    for node in nodes:
        deg = node.degree()
        if deg > max_deg:
            max_node = node
            max_deg = deg
    return max_node


def remove_node(nodes, targets, depth):
    for target in targets:
        target.disconnect_from_neighbours()
    for target in targets:    
        nodes.remove(target)
    #debug("done with remove_nodes", depth)
    return nodes

def neighbourhood(node):
    return [node] + list(node.neighbours)


def R0(nodes_in, depth=-1):
    depth += 1
    debug("R0({:s})".format(nodes_in), depth)
    nodes = copy.deepcopy(nodes_in)
    if len(nodes) == 0:
        debug("No nodes in input, returning 0", depth)
        return 0
    nu = contains_unconnected_node(nodes)
    if nu: 
        debug("Found unconnected {:s}. Returning 1 + G[V-nu].".format(nu), depth)
        return 1 + R0(remove_node(nodes, [nu], depth), depth)
    else:
        max_deg_node = maximum_degree(nodes)
        debug("Max deg node is {:s}".format(max_deg_node), depth)
        orig_nodes = copy.deepcopy(nodes)
        max_deg_node2 = maximum_degree(orig_nodes)
        debug("a = Recursing on G[V-N(maxdegnode)]", depth)
        a = R0(remove_node(nodes, neighbourhood(max_deg_node), depth), depth)
        debug("b = Recursing on G[V-maxdegnode]", depth)
        b = R0(remove_node(orig_nodes, [max_deg_node2], depth), depth)
        debug("a_max = {:d}, b_max = {:d}".format(1+a, b), depth)
        return max((1 + a), b)

def R1():
    pass

def R2():
    pass
