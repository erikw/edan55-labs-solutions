class Node:

    def __init__(self, number):
        self.id = number 
        self.neighbours = set()

    def add_edge(self, node):
        self.neighbours.add(node)

    def disconnect_from_neighbours(self):
        for neighbour in self.neighbours:
            neighbour.remove_edge_to(self)

        for neighbour in list(self.neighbours):
            self.remove_edge_to(neighbour)

    def remove_edge_to(self, target):
       # print("in node {:s}, removing edge to node {:d}".format(self, target.id))
        self.neighbours.remove(target)

    def degree(self):
        return len(self.neighbours)

    def __str__(self):
        return "node id: {:d} with neighbours {:s}".format(self.id, self.neighbours)

    def __repr__(self):
        return "node_id={:d}".format(self.id) 
