from binary_tree import TreeNode

class BST:
    def __init__(self):
        self.root=None

    def get_root(self):
        return self.root

    def preorder_traverse(self, cur, func, *args, **kwargs):
        if not cur:
            return

        func(cur, *args, **kwargs)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    def insert(self, key):
        new_node = TreeNode(key)

        cur = self.root

        # 노드(data)가 하나도 없다
        if not cur:
            self.root = new_node
            return

        # 무조건 노드가 하나는 있다
        while True:
            parent = cur
            if key < cur.key:
                cur = cur.left
                if not cur:
                    parent.left = new_node
                    return
            else:
                cur = cur.right
                if not cur:
                    parent.right = new_node
                    return


    def search(self, target):
        cur = self.root
        while cur:
            if cur.key == target:
                return cur
            elif target < cur.key:
                cur = cur.left
            elif target > cur.key:
                cur = cur.right
        return None

    def __remove_recursion(self, cur, target):
        if not cur:
            return None, None
        elif target < cur.key:
            cur.left, rem_node = self.__remove_recursion(cur.left, target)
        elif target > cur.key:
            cur.right, rem_node = self.__remove_recursion(cur.right, target)
        # 이제 삭제 노드를 찾았다!
        else:
            # 삭제 노드가 리프노드일 때
            if not cur.left and not cur.right:
                rem_node = cur
                cur = None
            # 삭제 노드의 자식 노드가 하나일때
            # 자식 노드가 왼쪽 자식 노드 일때
            elif not cur.right:
                rem_node = cur
                cur = cur.left
            # 삭제 노드의 자식 노드가 하나일때
            # 자식 노드가 오른쪽 자식 노드 일때
            elif not cur.left:
                rem_node = cur
                cur = cur.right
            else:
                replace_node = cur.left
                while replace_node.right:
                    replace_node = replace_node.right
                cur.key, replace_node.key = replace_node.key, cur.key
                cur.left, rem_node = self.__remove_recursion(cur.left, replace_node.key)
        return cur, rem_node

    def remove(self, target):
        self.root, removed_node = self.__remove_recursion(self.root, target)
        if removed_node:
            removed_node.left = removed_node.right = None
        return removed_node
        
if __name__=="__main__":
    print('*'*100)
    bst=BST()

    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    f=lambda x: print(x.key, end='  ')

    bst.preorder_traverse(bst.get_root(), f)
    print()

    searched = bst.search(15)
    if searched:
        print('searched data : {}'.format(searched))
    else:
        print('there is no such key({})'.format(searched))
    # 리프노드를 삭제할때
    # bst.remove(9)
    # 자식노드가 하나일때
    # bst.remove(8)
    # 자식노드가 두개 일때
    bst.remove(6)

    # print(bst.remove(15))

    bst.preorder_traverse(bst.get_root(), f)
    print()
    print('*'*100)