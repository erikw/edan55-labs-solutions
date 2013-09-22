class Graph:

    def __init__(self, nodes):
        self._version = 0
        self.nodes = nodes

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
        
