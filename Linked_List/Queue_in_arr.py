class Queue:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        self.container.pop(0)

    def peek(self):
        return self.container[0]

if __name__ == "__main__":
    q = Queue()
    
    for i in range(5):
        q.enqueue(i)
    
    for i in q.container:
        print(i)
    while not q.empty():
        print(q.dequeue(), end='   ')