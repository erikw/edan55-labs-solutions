import abc

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
