import copy
# TODO count calls to R0

def debug(text, depth):
    pass
    #print("{:s}{:s}".format('\t' * depth, text))

def R0(graph, depth=-1):
    depth += 1
    debug("R0({:s})".format([x for x in graph.nodes if x.exists_in(graph._version)]), depth)
    if graph.is_empty():
        debug("No nodes in input, returning 0", depth)
        return 0

    unconnected_node = graph.contains_unconnected_node()
    if unconnected_node: 
        debug("Found unconnected {:s}. Returning 1 + G[V-nu].".format(unconnected_node), depth)
        graph.new_version()        
        graph.remove_node([unconnected_node])
        mis_size = 1 + R0(graph, depth)
        graph.rewind_version();
        return mis_size
    else:
        max_deg_node = graph.maximum_degree()
        debug("Max deg node is {:s}".format(max_deg_node), depth)

        debug("a = Recursing on G[V-N(maxdegnode)]", depth)
        graph.new_version()
        graph.remove_node(graph.neighbourhood(max_deg_node))
        mis_a = 1 + R0(graph, depth)
        graph.rewind_version()

        debug("b = Recursing on G[V-maxdegnode]", depth)
        graph.new_version()
        graph.remove_node([max_deg_node])
        mis_b = R0(graph, depth)
        graph.rewind_version()

        debug("mis_a = {:d}, mis_b = {:d}".format(mis_a, mis_b), depth)
        return max(mis_a, mis_b)

def R1():
    pass

def R2():
    pass
