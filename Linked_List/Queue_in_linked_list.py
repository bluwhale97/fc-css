class Queue_Node:
    def __init__(self):
        self.__data = None
        self.__link = None

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def link(self):
        return self.__link
    @link.setter
    def link(self, link):
        self.__link = link

class Queue:
    def __init__(self):
        self.head = None
        self.rear = None
        self.d_size = 0

    def empty(self):
        '''
        empty(self)->Boolean
        '''
        if not self.d_size:
            return True
        else:
            return False

    def enqueue(self, data):
        '''
        enqueue(self,data) -> none
        queue의 맨 뒤에 데이터를 쌓는다.
        '''
        new_node = Queue_Node()
        new_node.data = data

        if not self.d_size:
            self.head = new_node
            self.rear = new_node
        else:
            self.rear.link = new_node
            self.rear = self.rear.link

        self.d_size += 1
        return None

    def dequeue(self):
        '''
        dequeue(self) - > node.data
        queue의 맨 앞에 데이터를 삭제하면서 반환한다.
        '''
        if not self.d_size:
            return None
        
        deleted_node = self.head
        self.head = self.head.link
        deleted_node.link = None

        self.d_size -= 1

        return deleted_node.data

    def peek(self):
        '''
        peek(self) -> node.data
        queue의 맨 앞 데이터를 삭제하지 않고 반환
        '''
        if not self.d_size:
            return None
        
        return self.head.data

if __name__ == "__main__":
    q = Queue()
    for i in range(5):
        q.enqueue(i)
    q.dequeue()
    print("empty is {}".format(q.empty()))
    print("peek is {}".format(q.peek()))
    print(q.peek())
    for i in range(5):
        print(q.empty())
        print(q.peek())
        q.dequeue()
    print(q.empty())
