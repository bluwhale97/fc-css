class Node:
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

class Stack:
    def __init__(self):
        self.head = None
        self.d_size = 0

    def empty(self):
        '''
        empty(None)->Boolean
        스택이 비어있는지 확인
        '''
        if not self.d_size:
            return True
        else:
            return False

    def push(self,data):
        '''
        push(data)->None
        스택의 top에 데이터를 쌓는다.
        '''
        new_node = Node()
        new_node.data = data

        self.head = new_node

        self.d_size += 1

    def pop(self):
        '''
        pop(None)->node.data
        Stack의 맨위 Node를 삭제하며 데이터를 반환한다.
        '''
        if not self.d_size:
            return None
        deleted_node = self.head
        deleted_node.link = None

        self.head = self.head.link

        self.d_size -= 1

        return deleted_node.data

    def peek(self):
        '''
        peek(None)->node.data
        '''
        return self.head.data

class Queue():
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()
        self.d_size = 0

    def empty(self):
        '''
        empty(self)->Boolean
        '''
        if not self.d_size:
            return True
        else :
            return False

    def enqueue(self, data):
        '''
        enqueue(self,data) -> none
        queue의 맨 뒤에 데이터를 쌓는다.
        '''
        self.enqueue_stack.push(data)
        self.d_size += 1

    def dequeue(self):
        '''
        dequeue(self) - > node.data
        queue의 맨 앞에 데이터를 삭제하면서 반환한다.
        '''
        if not self.dequeue_stack.d_size:
            for _ in range(self.enqueue_stack.d_size):
                self.dequeue_stack.push(self.enqueue_stack.pop)
        
        self.d_size -= 1
        return self.dequeue_stack.pop

    def peek(self):
        '''
        peek(self) -> node.data
        queue의 맨 앞 데이터를 삭제하지 않고 반환
        '''
        return self.enqueue_stack.peek()
