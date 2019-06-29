class MyQueue(object):

    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        popData = self.data[0]
        del self.data[0]
        return popData

    def peek(self):
        return self.data[0]

    def empty(self):
        return len(self.data) == 0
