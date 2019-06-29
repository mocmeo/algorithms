class MyStack(object):

    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.insert(0, x)

    def pop(self):
        popData = data[0]
        del data[0]
        return popData

    def top(self):
        return self.data[0]

    def empty(self):
        return len(self.data) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
obj.top()

print(obj.data)
