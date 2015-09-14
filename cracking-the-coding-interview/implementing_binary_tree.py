r"""
Implement a binary tree

        9
       / \
     5     3
    / \  / \
   1   3 4  6

"""


class BinaryTree(object):

    """ Binary tree implementation. """

    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, node):
        if not self.left:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t

    def insert_right(self, node):
        if not self.right:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def set_root(self, root):
        self.key = root

    def get_value(self):
        return self.key
