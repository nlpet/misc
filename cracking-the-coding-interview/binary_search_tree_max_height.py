"""Implement a binary search tree and find its max height"""
import unittest

class TestBST(unittest.TestCase):

    """Unit tests for counting numbers divisible by K."""

    def test_insert(self):
        """Test insert."""
        bst = BST()
        self.assertTrue(bst.insert(8))
        self.assertTrue(bst.insert(3))
        self.assertTrue(bst.insert(10))
        self.assertFalse(bst.insert(10))
        self.assertFalse(bst.insert(3))
        self.assertTrue(bst.insert(1))

    def test_find(self):
        """Test find."""
        bst = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        self.assertTrue(bst.find(10))
        self.assertTrue(bst.find(5))
        self.assertFalse(bst.find(11))
        self.assertFalse(bst.find(2))

    def test_traversals(self):
        """Test pre order."""
        bst = BST()
        bst.insert(8)
        bst.insert(3)
        bst.insert(10)
        bst.insert(1)
        bst.insert(6)
        bst.insert(14)
        bst.insert(4)
        bst.insert(7)
        bst.insert(13)
        self.assertEqual(bst.pre_order(), [8, 3, 1, 6, 4, 7, 10, 14, 13])
        self.assertEqual(bst.in_order(), [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(bst.post_order(), [1, 4, 7, 6, 3, 13, 14, 10, 8])

    def test_max_height(self):
        """Tests max height"""
        bst = BST()
        self.assertEqual(bst.find_max_height(), 0)
        bst.insert(8)
        bst.insert(3)
        self.assertEqual(bst.find_max_height(), 1)
        bst.insert(10)
        bst.insert(1)
        self.assertEqual(bst.find_max_height(), 2)
        bst.insert(6)
        bst.insert(14)
        self.assertEqual(bst.find_max_height(), 2)
        bst.insert(4)
        self.assertEqual(bst.find_max_height(), 3)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, value):
        if self.value == value:
            return True
        elif self.value > value:
            if self.left:
                return self.left.find(value)
            else:
                return False
        else:
            if self.right:
                return self.right.find(value)
            else:
                return False

    def pre_order(self, tree):
        if self.value:
            print self.value,
            tree.pre_order_lst.append(self.value)
            if self.left:
                self.left.pre_order(tree)
            if self.right:
                self.right.pre_order(tree)
        
    def post_order(self, tree):
        if self.value:
            if self.left:
                self.left.post_order(tree)
            if self.right:
                self.right.post_order(tree)
            print self.value,
            tree.post_order_lst.append(self.value)
        
    def in_order(self, tree):
        if self.value:
            if self.left:
                self.left.in_order(tree)
            print self.value,
            tree.in_order_lst.append(self.value)
            if self.right:
                self.right.in_order(tree)

    def find_max_height(self, tree):
        if self.left:
            tree.left_height += 1
            self.left.find_max_height(tree)
        if self.right:
            tree.right_height += 1
            self.right.find_max_height(tree)
        tree.max_height = max(tree.max_height, tree.left_height, tree.right_height)
            

class BST(object):
    def __init__(self):
        self.root = None
        self.left_height = 0
        self.right_height = 0
        self.max_height = 0
        self.pre_order_lst = []
        self.in_order_lst = []
        self.post_order_lst = []
        
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
            
    def find(self, value):
        if self.root:
            return self.root.find(value)
        else:
            return False
            
    def pre_order(self):
        if self.root:
            print "Pre-order traversal:"
            self.pre_order_lst = []
            self.root.pre_order(self)
            print ""
            return self.pre_order_lst
            
    def post_order(self):
        if self.root:
            print "Post-order traversal:"
            self.post_order_lst = []
            self.root.post_order(self)
            print ""
            return self.post_order_lst

    def in_order(self):
        if self.root:
            print "In-order traversal:"
            self.in_order_lst = []
            self.root.in_order(self)
            print ""
            return self.in_order_lst
            
    def find_max_height(self):
        if self.root:
            self.left_height = 0
            self.right_height = 0
            self.max_height = 0
            self.root.find_max_height(self)
            return self.max_height
        else:
            return 0


if __name__ == '__main__':
    unittest.main()
