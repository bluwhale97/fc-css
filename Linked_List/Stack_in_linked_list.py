class Stack_Node:
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
        new_node = Stack_Node()
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

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    tmp = s.peek()
    print(tmp)
    dl = s.pop()
    print(dl)
    flag = s.empty()
    print(flag)        
    