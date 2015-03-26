
'''
Implement a binary search tree

     9
    / \
   5   3 
  / \ / \
 1  3 4  6
 
'''


class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.size = 0
    
  def length(self):
    return self.size
    
  def __len__(self)
    return self.size
    
  def __iter__(self):
    return self.root.__iter__()
    
  
    
class TreeNode:
  def __init__(self, key, val, left=None, right=None, parent=None):
    self.key = key
    self.val = val
    self.left = left
    self.right = right
    self.parent = parent
    
  def has_left_child(self):
    return self.left
    
  def has_right_child(self):
    return self.right
    
  def is_left_child(self):
    return self.parent and self.parent.left == self
    
  def is_right_child(self):
    return self.parent and self.parent.right == self
    
  def is_root(self):
    return not self.parent
    
  def has_any_children(self):
    return self.left or self.right 
    
  def has_both_children(self):
    return self.left and self.right
    
  def replace_node_data(self, key, value, left, right):
    self.key = key
    self.payload = value
    self.left = left
    self.right = right
    if self.has_left_child():
      self.left.parent = self
    if self.has_right_child():
      self.right.parent = self
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  