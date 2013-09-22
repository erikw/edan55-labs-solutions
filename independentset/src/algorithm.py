import copy
# TODO count calls to R0

def debug(text, depth):
    pass
    #print("{:s}{:s}".format('\t' * depth, text))

def R0(graph, depth=-1):
    R0.nbr_calls += 1
    depth += 1
    debug("R0({:s})".format(graph.mates.keys()), depth)
    if graph.is_empty():
        debug("No nodes in input, returning 0", depth)
        return 0

    unconnected_node = graph.contains_unconnected_node()
    if unconnected_node is not None: 
        debug("Found unconnected {:d}. Returning 1 + G[V-nu].".format(unconnected_node), depth)
        graph.new_version()        
        graph.remove_node([unconnected_node])
        mis_size = 1 + R0(graph, depth)
        graph.rewind_version();
        return mis_size

    max_deg_node = graph.maximum_degree()
    debug("Max deg node is {:d}".format(max_deg_node), depth)

    graph.new_version()
    graph.remove_node(graph.neighbourhood(max_deg_node))
    debug("a = Recursing on G[V-N(maxdegnode)]", depth)
    mis_a = 1 + R0(graph, depth)
    graph.rewind_version()
    
    graph.new_version()
    graph.remove_node([max_deg_node])
    debug("b = Recursing on G[V-maxdegnode]", depth)
    mis_b = R0(graph, depth)
    graph.rewind_version()

    debug("mis_a = {:d}, mis_b = {:d}".format(mis_a, mis_b), depth)
    return max(mis_a, mis_b)

def R1(graph, depth=-1):
    R1.nbr_calls += 1
    depth += 1
    debug("R1({:s})".format(graph.mates.keys()), depth)
    if graph.is_empty():
        debug("No nodes in input, returning 0", depth)
        return 0

    unconnected_node = graph.contains_node_deg(0)
    if unconnected_node is not None: 
        debug("Found unconnected {:d}. Returning 1 + G[V-nu].".format(unconnected_node), depth)
        graph.new_version()
        graph.remove_node([unconnected_node])
        mis_size = 1 + R1(graph, depth)
        graph.rewind_version();
        return mis_size

    deg_one_node = graph.contains_node_deg(1)            
    if deg_one_node is not None:
        debug("Found node of deg 1 {:d}. Returning 1 + G[V-N[u]].".format(deg_one_node), depth)
        graph.new_version()        
        graph.remove_node(graph.neighbourhood(deg_one_node))
        mis_size = 1 + R1(graph, depth)
        graph.rewind_version();
        return mis_size

    max_deg_node = graph.maximum_degree()
    debug("Max deg node is {:d}".format(max_deg_node), depth)

    graph.new_version()
    graph.remove_node(graph.neighbourhood(max_deg_node))
    debug("a = Recursing on G[V-N(maxdegnode)]", depth)
    mis_a = 1 + R1(graph, depth)
    graph.rewind_version()
    
    graph.new_version()
    graph.remove_node([max_deg_node])
    debug("b = Recursing on G[V-maxdegnode]", depth)
    mis_b = R1(graph, depth)
    graph.rewind_version()

    debug("mis_a = {:d}, mis_b = {:d}".format(mis_a, mis_b), depth)
    return max(mis_a, mis_b)

def R2():
    pass
