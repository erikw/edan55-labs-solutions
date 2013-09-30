import inspect
import types

class Node:

    def __init__(self, number):
        self.id = number
        self.last_mod_version = 0
        self.neighbours = {0: set()}
        self.exists = {0 : True}

    # We happens to know that this func is only called when version=0 i.e. in the build up phase
    # TODO make more general...
    def add_edge(self, node, version = 0):
        self.neighbours[version].add(node)

#    def _update_version_strux(self, version):
#        if self.last_mod_version < version:
#            self.neighbours[version] = self.neighbours[self.last_mod_version].copy()
#            self.last_mod_version = version

    def disconnect_from_neighbours(self, version):
        #self._update_version_strux(version)
        for neighbour in self.neighbours[version]:
            neighbour.remove_edge_to(self, version)

        for neighbour in list(self.neighbours[version]):
            self.remove_edge_to(neighbour, version)

    def remove_edge_to(self, target, version):
        #self._update_version_strux(version)
        # print("in node {:s}, removing edge to node {:d}".format(self, target.id))
        self.neighbours[version].remove(target)

    def neighbourhood(self, version):
        return [self] + list(self.neighbours[version])

    def delete(self, version):
       self.exists[version] = False 

    def exists_in(self, version):
        return version in self.exists and self.exists[version]

    def degree(self, version):
        if self.exists_in(version):
            return len(self.neighbours[version])
        else:
            return -1

    def new_version(self, new_ver):
        if self.exists_in(new_ver - 1):
            self.exists[new_ver] = True
            self.neighbours[new_ver] = set()
            for x in self.neighbours[new_ver - 1]:
                if x.exists_in(new_ver - 1):
                    self.neighbours[new_ver].add(x)

    def rewind_version(self, old_ver):
        if self.exists_in(old_ver):
            del self.neighbours[old_ver]
            del self.exists[old_ver]

    def __str__(self):
        return "node id: {:d}".format(self.id)

    def __repr__(self):
        return "node_id={:d}".format(self.id) 
