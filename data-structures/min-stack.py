import sys


class MinStack(object):

    def __init__(self):
        self.data = []
        self.min = sys.maxsize

    def push(self, x):
        self.data.insert(0, x)
        self.min = min(self.min, x)

    def pop(self):
        popData = self.data[0]
        del self.data[0]
        self.min = min(self.data) if len(self.data) > 0 else sys.maxize
        return popData

    def top(self):
        return self.data[0]

    def getMin(self):
        return self.min
