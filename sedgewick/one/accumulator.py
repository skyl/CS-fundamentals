class Accumulator(object):

    def __init__(self):
        self.N = 0
        self.total = 0

    def __str__(self):
        return "Mean for {N} values = {mean}".format(
            N=self.N, mean=self.mean())

    def add_value(self, val):
        self.total += val
        self.N += 1

    def mean(self):
        if self.N == 0:
            return None
        return self.total / self.N
