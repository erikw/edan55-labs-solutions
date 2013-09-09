import abc
import random

class RandProc(metaclass=abc.ABCMeta):
    def __init__(self, name, nbr_gens):
        self.name = name
        self._nbr_gens = nbr_gens

    @abc.abstractmethod
    def __str__(self):
        return "Random process \"%s\".".format(self.name)

    __repr__ = __str__

    @abc.abstractmethod
    def next_nbr(self, marker):
        pass

class R1(RandProc):
    def __init__(self, *args, **kwargs):
        super(R1, self).__init__("R1", *args, **kwargs)

    def __str__(self):
        return super(R1, self).__str__() + "I'm random 1 -- uniform(1, N)."

    __repr__ = __str__

    def next_nbr(self, marker):
        return random.randint(0, marker.nbr_nodes - 1)

class R2(RandProc):

    def __init__(self, *args, **kwargs):
        super(R2, self).__init__("R2", *args, **kwargs)
        self._permutation = self._gen_knuth_nbrs()
        #print(self._permutation)
        self._perm_iter_pos = -1

    # Inside-out version https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_.22inside-out.22_algorithm
    def _gen_knuth_nbrs(self):
        N = self._nbr_gens
        output = [0] + [None] * (N - 1)
        #print("outputlen = {:d}, N = {:d}".format(len(output), N))
        for output_pos in range(1, N):
            rnd_pos = random.randint(0, output_pos)
            output[output_pos] = output[rnd_pos]
            output[rnd_pos] = output_pos
        return output


    def __str__(self):
        return super(R2, self).__str__() + "I'm random 2 -- Knuth Shuffle."

    __repr__ = __str__

    def next_nbr(self, marker):
        self._perm_iter_pos += 1
        #print(self._perm_iter_pos)
        return self._permutation[self._perm_iter_pos]

class R3(RandProc):
    def __init__(self, *args, **kwargs):
        super(R3, self).__init__("R3", *args, **kwargs)

    def __str__(self):
        return super(R3, self).__str__() + "I'm random 3 -- uniformly(non_marked_nodes)."

    __repr__ = __str__

    def next_nbr(self, marker_r3):
        return marker_r3.unmarked[random.randint(0, marker_r3.unmarked_active_elems - 1)]
