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

        if self.empty():
            self.head = new_node
        else:
            new_node.link = self.head
            self.head = new_node

        self.d_size += 1

    def pop(self):
        '''
        pop(None)->node.data
        Stack의 맨위 Node를 삭제하며 데이터를 반환한다.
        '''
        if not self.d_size:
            return 
        deleted_node = self.head
        self.head = self.head.link
       
        deleted_node.link = None

        self.d_size -= 1

        return deleted_node.data

    def peek(self):
        '''
        peek(None)->node.data
        '''
        return self.head.data

def show(s):
    cur = s.head
    while cur:
        print('{} is data'.format(cur.data))
        cur = cur.link

if __name__ == "__main__":
    s = Stack()
    for i in range(5):
        s.push(i)
    show(s)
    print("{} is poped".format(s.pop()))
    print("{} is poped".format(s.pop()))
    
    
    for i in range(s.d_size):
        dl = s.pop()
    
    print(dl)
    flag = s.empty()
    print('empty is {}'.format(flag))        
