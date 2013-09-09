def mark_counter(mark_func):
    def counter(marker, number):
        marker.mark_count += 1
        return mark_func(marker, number)
    return counter

class Marker:
    def __init__(self, tree_height):
        self._height = tree_height
        self.mark_count = 0
        self.nbr_nodes = 2**self._height - 1
        self.marked = set()

    def _all_marked(self):
        return len(self.marked) == self.nbr_nodes

    def _mark_node(self, node):
        self.marked.add(node)

    def _is_leaf(self, number):
        return number >= (self.nbr_nodes / 2)

    @staticmethod
    def _is_root(number):
        return number == 0

    @staticmethod
    def _child_type(number):
        if number % 2 == 0:
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
        #if number in self.marked:
            #return
        self._mark_node(number)
        #print("{:d}\tx\tMarked by Bob.".format(number))
        if not self._is_leaf(number):
            (child_l, child_r) = self._children_of(number)
            if child_l in self.marked and child_r not in self.marked:
                self._mark_cascade(child_r)
            elif child_r in self.marked and child_l not in self.marked:
                self._mark_cascade(child_l)

        if not self._is_root(number):
            parent = self._parent_of(number)
            (parent_lchild, parent_rchild) = self._children_of(parent)
            if parent in self.marked:
                if self._child_type(number) == 'left' and not parent_rchild in self.marked:
                    self._mark_cascade(parent_rchild)
                elif not parent_lchild in self.marked:
                    self._mark_cascade(parent_lchild)
            else:
                if parent_lchild in self.marked and parent_rchild in self.marked:
                    self._mark_cascade(parent)

    @mark_counter
    def _mark(self, number):
        self._mark_cascade(number)

    def run(self, rand_proc):
        while not self._all_marked():
            #self._mark(rand_proc.next_nbr(self))
            next_nbr = rand_proc.next_nbr(self)
            #print("{:d}\t-> \tSent by Alice.".format(next_nbr))
            self._mark(next_nbr)


    def status(self):
        return "send count = {:d}".format(self.mark_count)


class MarkerR3(Marker):
    def __init__(self, *args, **kwargs):
        super(MarkerR3, self).__init__(*args, **kwargs)
        self.unmarked = [i for i in range(0, self.nbr_nodes)]
        self.unmarked_active_elems = self.nbr_nodes
        self._unmarked_pos = {}

    def _mark_node(self, node):
        super(MarkerR3, self)._mark_node(node)
        if node not in self._unmarked_pos:
            node_pos = node
        else:
            node_pos = self._unmarked_pos[node]
        self.unmarked[node_pos], self.unmarked[self.unmarked_active_elems - 1] = \
                self.unmarked[self.unmarked_active_elems - 1], self.unmarked[node_pos]
        self.unmarked_active_elems -= 1
        self._unmarked_pos[self.unmarked[node_pos]] = node_pos
