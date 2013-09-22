import inspect
import types

class Node:

    def __init__(self, number):
        self.id = number

    def __str__(self):
        return "node id: {:d}".format(self.id)

    def __repr__(self):
        return "node_id={:d}".format(self.id)
