class Stack:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()
        

    def peek(self):
        return self.container[-1]

s=Stack()

for i in range(5):
    s.push(i)

while not s.empty():
    print(s.pop(), end='  ')