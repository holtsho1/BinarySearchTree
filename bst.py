#https://gist.github.com/TheDataLeek/4689217
#http://chinmayakrpatanaik.com/2016/06/01/Binary-Search-Tree-Python/
#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-index.php


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root
        
    def init_node(self, data):
        """
        Create and return a bt_node object that has been initialized
        with the given data and two None children.
        """
        new_node      = Node()
        new_node.data = data
        return new_node

    def get_root(self):
        return self.root

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            node = self.root
            while node is not None:
                if item < node.data:
                    if node.left is None:
                        node.left = Node(item)
                        return
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(item)
                        return
                    else:
                        node = node.right

    def insert_data(self, data):
        """
        Insert a new node that contains the given data into the tree
        at the correct location.
        """
        new_node = self.init_node(data)
        self.insert(new_node)

    def remove(self, data):
        """
        Removes a node from the tree whose data value is the same as
        the argument.
        """
        if self.contains(data):
            cursor = self.root
            parent = None
            while True:
                if cursor.data == data:
                    break
                elif cursor.data > data:
                    parent = cursor
                    cursor = cursor.left
                elif cursor.data < data:
                    parent = cursor
                    cursor = cursor.right
            if cursor.right and cursor.left:
                successor, successor_parent = self.find_successor(cursor)
                predecessor, predecessor_parent = self.find_predecessor(cursor)
                self.to_array()
                if len(self.root_list) % 2 == 0:
                    if successor_parent:
                        cursor.data = successor.data
                        self.delete_node(successor, successor_parent)
                    else:
                        cursor.data = successor.data
                        self.delete_node(successor, cursor)
                else:
                    if predecessor_parent:
                        cursor.data = predecessor.data
                        self.delete_node(predecessor, predecessor_parent)
                    else:
                        cursor.data = predecessor.data
                        self.delete_node(predecessor, cursor)
            else:
                if parent:
                    self.delete_node(cursor, parent)
                else:
                    try:
                        successor, successor_parent = self.find_successor(cursor)
                    except AttributeError:
                        predecessor, predecessor_parent = self.find_predecessor(cursor)
                    if successor:
                        cursor.data = successor.data
                        self.delete_node(successor, cursor)
                    else:
                        cursor.data = predecessor.data
                        self.delete_node(predecessor, cursor)

    def delete_node(self, node, parent):
        '''
        Deletes specified node with specified parent
        Should not be called
        '''
        try:
            if parent.left == node:
                if node.left:
                    parent.left = node.left
                elif node.right:
                    parent.left = node.right
                else:
                    parent.left = None
            elif parent.right == node:
                if node.left:
                    parent.right = node.left
                elif node.right:
                    parent.right = node.right
                else:
                    parent.right = None
            else:
                if parent.left == node:
                    parent.left = None
                if parent.right == node:
                    parent.right = None
        except AttributeError:
            print sys.exc_info()
            print '    ', self.to_array()
            print '	', node.data
            sys.exit(1)

    def find_successor(self, node):
        '''
        Finds the in-order successor of the given node
        '''
        successor_node = node.right
        successor_top  = None
        while True:
            if successor_node.left == None:
                break
            else:
                successor_top = successor_node
                successor_node = successor_node.left
        return successor_node, successor_top

    def find_predecessor(self, node):
        '''
        Finds the in-order predecessor of the given node
        '''
        predecessor_node = node.left
        predecessor_top  = None
        while True:
            if predecessor_node.right == None:
                break
            else:
                predecessor_top = predecessor_node
                predecessor_node = predecessor_node.right
        return predecessor_node, predecessor_top

    def contains(self, data):
        """
        Return True or False depending on if this tree contains a node
        with the supplied data.
        """
        if self.root is None:
            return False
        else:
            cursor = self.root
            while True:
                if data < cursor.data:
                    if cursor.data == data:
                        return True
                    if cursor.left is None:
                        return False
                    else:
                        cursor = cursor.left
                if data >= cursor.data:
                    if cursor.data == data:
                        return True
                    if cursor.right is None:
                        return False
                    else:
                        cursor = cursor.right

    def get_node(self, data):
        """
        If the tree contains a node with the supplied data, return
        it. Otherwise return None.
        """
        if self.contains(data):
            cursor = self.root
            while True:
                if data < cursor.data:
                    cursor = cursor.left
                if data >= cursor.data:
                    if cursor.data == data:
                        return cursor
                    else:
                        cursor = cursor.right
        else:
            return None

    def to_array(self):
        """
        Create and fill a list with the data contained in this
        tree. The elements of the returned list must be in the same
        order as they are found during an inorder traversal, which
        means the numbers should be in non-decreasing order.
        """
        if self.root is None:
            return []
        else:
            self.tree_list  = []
            self.tree_nodes = []
            self.search(self.root)
            return self.tree_list

    def search(self, node, item):
       if node is None:
           return False
       else:
           if node.data == item:
               return True
           elif node.data < item:
               return self.search(node.right, item)
           else:
               return self.search(node.left, item)self, node):
    def size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)
        
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print node.data
            self.inorder(node.right)
            
    def preorder(self, node):
        if node:
            print node.data
            self.preorder(node.left)
            self.preorder(node.right)
            
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.data

    def closest_value(self, node, target):
        a = node.data
        kid = node.left if target < a else node.right
        if not kid:
            return a
        b = closest_value(kid, target)
        return min((a,b), key=lambda x: abs(target-x))

    def get_min(self, node):
        if node.left is None:
            return node.data
        else:
            return self.get_min(node.left)
        
    def get_max(self, node):
        if self.root is None:
            return "Tree is empty."
        else:
            if node.right is None:
                return node.data
            else:
                return self.get_max(node.right)
