#!/usr/bin/env python
#https://gist.github.com/TheDataLeek/4689217
#http://chinmayakrpatanaik.com/2016/06/01/Binary-Search-Tree-Python/

import sys
import unittest

from bst import Node, BinarySearchTree

class BstTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BstTest, self).__init__(*args, **kwargs)
        self.tree = BinarySearchTree()
        self.arr = [100, 20, 500, 30, 10, 40]

    def setUp(self):
        self.bst = BinarySearchTree()
        self.node_2 = self.bst.init_node(-2)
        self.node_1 = self.bst.init_node(-1)
        self.node0 = self.bst.init_node(0)
        self.node1 = self.bst.init_node(1)
        self.node2 = self.bst.init_node(2)
        self.node3 = self.bst.init_node(3)

        self.mytree = BinarySearchTree()
        self.mytree.insert_data(100)
        self.mytree.insert_data(20)
        self.mytree.insert_data(500)
        self.mytree.insert_data(30)
        self.mytree.insert_data(10)
        self.mytree.insert_data(40)

    def test_init_node(self):
        node1 = self.bst.init_node(5)
        node2 = self.bst.init_node(4)
        assert(node1.data  == 5)
        assert(node1.left  == None)
        assert(node1.right == None)
        assert(node2.data  == 4)
        assert(node2.left  == None)
        assert(node2.right == None)

    def test_insert(self):
        assert(self.bst.tree == None)
        self.bst.insert(self.node0)
        assert(self.bst.tree.data == self.node0.data)
        self.bst.insert(self.node3)
        assert(self.bst.tree.right.data == self.node3.data)
        self.bst.insert(self.node5)

    def test_contains(self):
        assert(self.mytree.contains(500) == True)
        assert(self.mytree.contains(40) == True)
        assert(self.mytree.contains(30) == True)

        assert(self.mytree.contains(80)  == False)
        assert(self.mytree.contains(-5)  == False)
        assert(self.mytree.contains(-10) == False)
        
    def test_search(self):
        self.assertTrue(self.tree.search(self.tree.get_root(), 30))
        self.assertFalse(self.tree.search(self.tree.get_root(), 12312))

    def test_size(self):
        self.assertEqual(self.tree.size(self.tree.get_root()), 6)

    def test_min(self):
        self.assertEqual(self.tree.get_min(self.tree.get_root()), 10)

    def test_max(self):
        self.assertEqual(self.tree.get_max(self.tree.get_root()), 500)

    def test_display(self):
        print "Inorder Traversal: "
        self.tree.inorder(self.tree.get_root())
        print "Preorder Traversal: "
        self.tree.preorder(self.tree.get_root())
        print "Postorder Traversal: "
        self.tree.postorder(self.tree.get_root())


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
