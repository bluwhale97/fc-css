class Node:
    def __init__(self):
        self.__data = None
        self.__link = None
    
    # garbage collector가 치우는것을 보기위한 소멸자
    def __del__(self):
        print('{} is deleted'.format(self.__data))

    # encapsulation
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, d):
        self.__data = d

    @property
    def link(self):
        return self.__link
    @link.setter
    def link(self, l):
        self.__link = l

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False
    
    def size(self):
        return self.d_size

    # insert
    def add(self, data):
        # 새로운 노드 생성
        # 데이터 저장
        new_node = Node()
        new_node.data = data
        
        new_node.link = self.head
        self.head = new_node

        self.d_size += 1


    # search
    def search(self, target):
        cur = self.head
        while cur:
            if cur.data == target:
                return cur 
            cur = cur.link
            return cur

    # delete
    def delete(self):
        # 첫번째 노드 삭제
        self.head = self.head.link
        self.d_size -= 1

# show_list
def show_list(singlelist):
    cur = singlelist.head
    for _ in range(singlelist.size()):
        print(cur.data, end='  ')
        cur = cur.link
    print()
sl = SingleLinkedList()

sl.add(1)
sl.add(2)
sl.add(3)
sl.add(4)
sl.add(5)

show_list(sl)


obj = sl.search(3)
if obj:
    print('{} is in the list.'.format(obj.data))
else:
    print('there is no such data')

sl.delete()
show_list(sl)
