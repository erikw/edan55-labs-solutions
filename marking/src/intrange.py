import argparse
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


