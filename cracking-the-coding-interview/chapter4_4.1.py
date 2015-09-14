r"""
Implement a function to check if a tree is balanced. For the purposes of this
question, a balanced tree is defined to be a tree such that no two leaf nodes
differ in distance from the root by more than one.


         1
        / \
       /   \
      /     \
     2       3
    / \     /
   4   5   6
  /       / \
 7       8   9


preorder:    1 2 4 7 5 3 6 8 9
inorder:     7 4 2 5 1 8 6 9 3
postorder:   7 4 5 2 8 9 6 3 1
level-order: 1 2 3 4 5 6 7 8 9
"""

class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
