r"""
Implement a binary search tree.

     9
    / \
   5   3
  / \ / \
 1  3 4  6

"""


class BinarySearchTree:

    """Binary search tree."""

    def __init__(self):
        """Initialize."""
        self.root = None
        self.size = 0

    def __len__(self):
        """Get length."""
        return self.size

    def __iter__(self):
        """Return an iterator."""
        return self.root.__iter__()


class TreeNode:

    """Treenode class."""

    def __init__(self, key, val, left=None, right=None, parent=None):
        """Initialize."""
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def has_left_child(self):
        """Return true if there exists a left child."""
        return self.left

    def has_right_child(self):
        """Return true if there exists a right child."""
        return self.right

    def is_left_child(self):
        """Return true if node is a left child."""
        return self.parent and self.parent.left == self

    def is_right_child(self):
        """Return true if node is a right child."""
        return self.parent and self.parent.right == self

    def is_root(self):
        """Return true if node is the root node."""
        return not self.parent

    def has_any_children(self):
        """Return true if node has children."""
        return self.left or self.right

    def has_both_children(self):
        """Return true if node has both children."""
        return self.left and self.right
