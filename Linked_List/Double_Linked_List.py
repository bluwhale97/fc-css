class Node:
    def __init__(self):
        self.__prev = None
        self.__next = None
        self.__data = None
    
    @property
    def prev(self):
        return self.__prev
    @prev.setter
    def prev(self,prev):
        self.__prev = prev
    
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, next):
        self.__next = next
    
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self,data):
        self.__data = data

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    
        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    # insert 계열
    def add_first(self, data):
        new_node = Node()
        new_node.data = data

        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

        self.d_size += 1

    def add_last(self, data):
        new_node = Node()
        new_node.data = data

        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.d_size += 1

    def insert_before(self, data, node):
        new_node = Node()
        new_node.data = data

        new_node.prev = node.prev
        new_node.next = node

        node.prev.next = new_node
        node.prev = new_node
        
        self.d_size += 1

    def insert_after(self, data, node):
        new_node = Node()
        new_node.data = data

        new_node.prev = node
        new_node.next = node.next

        node.next.prev = new_node
        node.next = Node

        self.d_size += 1

    def search_forward(self, target):
        cur = self.head.next

        while cur is not self.tail:
            if cur.data == target:
                return cur
            cur = cur.next
        return None

    def search_backward(self, target):
        cur = self.tail.prev

        while cur is not self.head:
            if cur.data == target:
                return cur
            cur = cur.next
        return None

    def delete_first(self):
        if self.empty():
            return
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        self.d_size -= 1

    def delete_last(self):
        if self.empty():
            return
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        self.d_size -= 1

    def delete_node(self, node):
        if (node is self.head) or (node is self.tail):
            return
        node.prev.next = node.next
        node.next.prev = node.prev

        self.d_size -= 1

if __name__ == "__main__":

    def show_list(dl):
        cur = dl.head.next
        while cur is not dl.tail:
            print(cur.data, end='   ')
            cur = cur.next

    dl = DoubleLinkedList()
    for i in range(5):
        dl.add_first(i)
    for i in range(-10,-5):
        dl.add_last(i)

    for i in range(3):
        tmp = dl.search_forward(i)
        dl.delete_node(tmp)

    dl.search_backward(100)
    show_list(dl)
