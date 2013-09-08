#import networkx as nx
#import matplotlib.pyplot as plt

def mark_counter(mark_func):
    def counter(marker, number):
        marker.mark_count += 1
        #print("decorating on markNo {:d}".format(number))
        return mark_func(marker, number)
    return counter

class Marker:
    def __init__(self, tree_height):
        self._height = tree_height
        #self._g = nx.balanced_tree(2, tree_height - 1)
        self.mark_count = 0
        #nx.freeze(self._g)
        #self.nbr_nodes = self._g.number_of_nodes()
        self.nbr_nodes = 2**self._height - 1
        self.marked = set()
        self.unmarked = set([i for i in range(0, self.nbr_nodes)])
        #for node in self._g.nodes_iter(data=True):
            #node[1]['marked'] = False
            ##print(node)

    def all_marked(self):
        return len(self.marked) == self.nbr_nodes

    def _mark_node(self, node):
        self.marked.add(node)
        self.unmarked.remove(node)

    def _is_leaf(self, number):
        return number >= (self.nbr_nodes / 2)

    @staticmethod
    def _is_root(number):
        return number == 0

    @staticmethod
    def _child_type(number):
        if self.nbr_nodes % 2 == 0:
            return 'right'
        else:
            return 'left'

    @staticmethod
    def _children_of(parent):
        base = parent * 2
        return base + 1, base + 2

    @staticmethod
    def _parent_of(child):
        return int((child - 1) / 2)

    def _mark_cascade(self, number):
        if number in self.marked:
            return
        print("{:d}\tx\tMarked by Bob.".format(number))
        self._mark_node(number)
        if not self._is_leaf(number):
            (child_l, child_r) = self._children_of(number)
            # case 1,2(children)
            if child_l in self.marked and child_r not in self.marked:
                self._mark_cascade(child_r)
            elif child_r in self.marked and child_l not in self.marked:
                self._mark_cascade(child_l)


        if self._is_root(number):
            parent = self._parent_of(number)
            #  case 3(parent)
            if not parent in self.marked:
                (parent_lchild, parent_rchild) = self._children_of(parent)
                if self._child_type(number) == "left":
                    if parent_rchild in self.marked:
                        self._mark_cascade(parent)
                else:
                    if parent_lchild in self.marked:
                        self._mark_cascade(parent)

    @mark_counter
    def mark(self, number):
        self._mark_cascade(number)



    def status(self):
        return "nbr_marked = {:d}\nsend count = {:d}".format(len(self.marked), self.mark_count)














    #print(G.number_of_nodes())
        #print(G.number_of_edges())
        #print(G.nodes())

    #nx.draw(G)
    #nx.draw_spectral(G)
    #plt.show()
