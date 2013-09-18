
#counts = [0, 0, 0]
#def count_calls(count_index):
#   def counter(alg_func, *args):
#        counts[count_index] += 1
#        alg_func(args)
#    return counter
     
def contains_unconnected_node(nodes):
    print("in contains")
    pass

def maximum_degree(nodes):
    print("in maxdeg")
    pass

def remove_node(nodes, target):
    print("in remove")
    pass

def neighbourhood(node):
    print("in neight")   
    pass


def R0(nodes):
    if len(nodes) == 0:
        return 0
    nu = contains_unconnected_node(nodes)
    if nu:
        return 1 + R0(remove_node(nodes, [nu]))
    else:
        max_deg_node = maximum_degree(nodes)
        return max(
                    (1 + R0(remove_node(nodes, neighbourhood(max_deg_node)))),
                    (1 + R0(remove_node(nodes, [max_deg_node])))
                )

def R1():
    pass

def R2():
    pass
