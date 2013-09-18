class Node:

    def __init__(self, number):
        self.id = number 
        self.neighbours = set()

    def add_edge(self, node):
        self.neighbours.add(node)

    def __str__(self):
        return "node id: {:d} with neighbours {:s}".format(self.id, self.neighbours)

    def __repr__(self):
        return "node id: {:d}".format(self.id) 
