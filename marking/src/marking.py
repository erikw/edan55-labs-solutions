#!/usr/bin/env python3
# Marking lab in EDAN55.

__author__ = "Erik Westrup"
__email__ = "erik.westrup@gmail.com"

import sys
import abc
import networkx as nx
import argparse
import matplotlib.pyplot as plt

class RandProc(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self._name = name

    @abc.abstractmethod
    def __str__(self):
        return "Random process \"%s\".".format(self._name)

    __repr__ = __str__

    @abc.abstractmethod
    def fun():
        pass

class R1(RandProc):
    def __init__(self, *args, **kwargs):
        super(R1, self).__init__("R1", *args, **kwargs)

    def __str__(self):
        return super(R1, self).__str__() + "I'm random 1."

    __repr__ = __str__

    def fun():
        pass

class R2(RandProc):
    def __init__(self, *args, **kwargs):
        super(R2, self).__init__("R2", *args, **kwargs)

    def __str__(self):
        return super(R2, self).__str__() + "I'm random 2."

    __repr__ = __str__

    def fun():
        pass

class R3(RandProc):
    def __init__(self, *args, **kwargs):
        super(R3, self).__init__("R3", *args, **kwargs)

    def __str__(self):
        return super(R3, self).__str__() + "I'm random 3."

    __repr__ = __str__

    def fun():
        pass

# Stolen from http://stackoverflow.com/questions/11272806/pythons-argparse-choices-constrained-printing 
class IntRange(object):
    def __init__(self, start, stop=None):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop = start, stop

    def __call__(self, value):
        value = int(value)
        if value < self.start or value > self.stop:
            raise argparse.ArgumentTypeError("value outside of range [{:d}, {:d}]".format(self.start, self.stop))
        return value

def parse_args():
    parser = argparse.ArgumentParser(description="Mark trees according to different random processes.")
    parser.add_argument("-r", "--random-proc", type=IntRange(1, 3), default=1, help="Which random process to use of R[1-3]")
    parser.add_argument("-H", "--tree-height", type=IntRange(1, float("inf")), default=3, help="Height h of the complete bin tree.")
    args = parser.parse_args()
    rand_proc = {
            1 : R1(),
            2 : R2(),
            3 : R3()
            }[args.random_proc]
    return rand_proc, (args.tree_height - 1)

def main():
    (rand_proc, tree_height) = parse_args()
    G = nx.balanced_tree(2, tree_height)
    print(G.number_of_nodes())
    print(G.number_of_edges())

    #print(G.nodes())
    #nx.draw(G)
    #nx.draw_spectral(G)
    #plt.show()


    return 0


if __name__ == '__main__':
    sys.exit(main())
