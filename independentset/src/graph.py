class Graph:
    def __init__(self, node_ids):
        self._version = -1
        self._deleted_edges = {} # version -> [(deleted_node,node)]
        self._added_edges = {} # version -> [(added_node,node)]
        self.mates = {node : set() for node in node_ids} # node -> set of node
        self._next_id = len(node_ids)
        self.new_version()
        

    def add_edge(self, node1, node2):
        if node1 not in self.mates:
            self.mates[node1] = set()
        self.mates[node1].add(node2)  
        if node2 not in self.mates:
            self.mates[node2] = set()
        self.mates[node2].add(node1)
        self._added_edges[self._version].append((node1, node2))

    def add_node(self):
        self.mates[self._next_id] = set()
        self._next_id +=1
        return self._next_id - 1
 
    def maximum_degree(self):
        max_deg = 0
        max_node = None
        for node, mates in self.mates.items():
            if len(mates) > max_deg:
                max_node = node
                max_deg = len(mates)
        return max_node

    def size(self):
        return len(self.mates)

    def contains_node_deg(self, degree):
        for node, mates in self.mates.items():
            if len(mates) == degree:
                return node
        return None

    def is_disconnected(self):
        for node, mates in self.mates.items():
            if len(mates) is not 0:
                return False
        return True

    def is_empty(self):
        return len(self.mates) == 0

    def new_version(self):
        self._version += 1
        self._deleted_edges[self._version] = []
        self._added_edges[self._version] = []

    def rewind_version(self):
        for node1, node2 in self._deleted_edges[self._version]:
            if node1 not in self.mates:
                self.mates[node1] = set()
            self.mates[node1].add(node2)
            if node2 not in self.mates:
                self.mates[node2] = set()
            self.mates[node2].add(node1)
        del self._deleted_edges[self._version]

        for node1, node2 in self._added_edges[self._version]:
           self.mates[node2].remove(node1)
        for node1, node2 in self._added_edges[self._version]:
            if node1 in self.mates:                       
                del self.mates[node1]
        del self._added_edges[self._version]

        if self._version is not 0:
            self._version -= 1

    def neighbourhood(self, target):
        if target in self.mates:
            return [target] + list(self.mates[target])
        else:
            return [target]

    def mates_of(self, node):
        return self.mates[node]

    def nodes_are_connected(self, node1, node2):
        return node1 in self.mates[node2]
        
    def _disconnect_from_mates(self, target):
        for mate in self.mates[target]:
            self.mates[mate].remove(target)
            self._deleted_edges[self._version].append((target, mate))

    def remove_node(self, targets):
        for target in targets:
            self._disconnect_from_mates(target)
        for target in targets:
            del self.mates[target]

    def __str__(self):
        out = "Graph of size {:d}, with nodes: {:s}\nEdges:\n".format(len(self.mates), self.mates.keys())
        for (node, mates) in self.mates.items():
            out += "{:d} -> {:s}\n".format(node, mates)
        return out       
