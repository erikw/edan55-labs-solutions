from node import Node

class Graph:

    def __init__(self):
        self._version = 0
        self.nodes = {} # nodeID -> NodeObject # TODO needed?
        self.mates = {} # node -> set of NodeObjects

    def add_edge(self, node1_id, node2_id):
        if node1_id not in self.nodes:
            self.nodes[node1_id] = Node(node1_id)
        node1 = self.nodes[node1_id]

        if node2_id not in self.nodes:
            self.nodes[node2_id] = Node(node2_id)
        node2 = self.nodes[node2_id]

        if node1 not in self.mates:
            self.mates[node1] = set()
        self.mates[node1].add(node2)
            
        if node2 not in self.mates:
            self.mates[node2] = set()
        self.mates[node2].add(node1)
 
    def maximum_degree(self):
        max_deg = 0
        for node in self.nodes:
            deg = node.degree(self._version)
            if deg > max_deg:
                max_node = node
                max_deg = deg
        return max_node

    def contains_unconnected_node(self):
        for node in self.nodes:
            if node.degree(self._version) == 0:
                return node
        return None

    def is_empty(self):
        for node in self.nodes:
            if node.exists_in(self._version):
                return False
        return True


    def remove_node(self, targets):
        for target in targets:
            target.disconnect_from_neighbours(self._version)
        for target in targets:
            target.delete(self._version)

    def neighbourhood(self, target):
        return target.neighbourhood(self._version)

    def new_version(self):
        self._version += 1
        for node in self.nodes:
            node.new_version(self._version)

    def rewind_version(self):
        for node in self.nodes:
            node.rewind_version(self._version)
        if self._version is not 0:
            self._version -= 1

    def __str__(self):
        out = "Graph of size {:d}, with nodes: {:s}\nEdges:\n".format(len(self.nodes), self.nodes)
        for (node, mates) in self.mates.items():
            out += "{:s} -> {:s}\n".format(node, mates)
        return out
        
