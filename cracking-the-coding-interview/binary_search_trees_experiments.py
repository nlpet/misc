# -*- coding: utf-8 -*-

import math
import Queue
from StringIO import StringIO


class Node(object):
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def print_tree(self):
        """
        Print tree content inorder
        """
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def tree_data(self):
        """
        Generator to get the tree nodes data
        """
        # we use a stack to traverse the tree in a non-recursive way
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                # we are returning so we pop the node and we yield it
                node = stack.pop()
                yield node.data
                node = node.right

# --------------------------------------- #

def flatten_to_list(root, l=[]):
    if not root:
        return
    flatten_to_list(root.left, l)
    l.append(root.data)
    flatten_to_list(root.right, l)
    return l


def traverse_linearly(root, l=[], q=Queue.Queue()):
    # add current node to list
    l.append(root.data)
    # if left and right nodes, add to queue
    if root.left:
        q.put(root.left)
    if root.right:
        q.put(root.right)

    # if queue not empty, process them
    if not q.empty():
        root = q.get()
        traverse_linearly(root)
    return l


def show_tree(tree, total_width=35, fill=' '):
    """Pretty-print a tree."""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    print()
    return


def pprint_binary_tree(tree):
    lvl_n = 0
    lvl_l = 1
    tree_l = len(tree)
    leaf_nodes_l = tree_l / 2

    while lvl_n <= leaf_nodes_l:
        s = ' ' * (tree_l/lvl_l+1)
        print(''.join([s+str(x)+s[:len(s)/2] for x in tree[lvl_n:lvl_n+lvl_l]]))
        lvl_n += lvl_l
        lvl_l *= 2


def pprint_structure(tree):

    tree_l = len(tree)
    leaf_nodes_l = tree_l / 2

    printed = []
    s1 = '        '
    s2 = '         '

    print(' └── ' + str(tree[0]))
    printed.append(tree[0])

    print(s2 + '├── ' + str(tree[1]))
    print(s2 + '|' + s1 + '└── ' + str(tree[3]))
    print(s2 + '|' + s1 + '└── ' + str(tree[4]))
    print(s2 + '├── ' + str(tree[2]))
    print(s2 + '|' + s1 + '└── ' + str(tree[5]))
    print(s2 + '|' + s1 + '└── ' + str(tree[6]))


# -==-----------------------==-
# Generate trees and print them

data = [70, 31, 93, 14, 73, 94, 23]

tree = Node(data[0])
for n in data[1:]:
    tree.insert(n)

print('\nSorted tree:')
tree.print_tree()
print('\n')

print('Tree level by level:')
l = traverse_linearly(tree)
print(' '.join([str(n) for n in l]))
print('\n')


print('Visual representation of the tree structure:')
total_width = len(l) * 6
show_tree(l, total_width)

# print ''
# print "Prettier visual representation:"
# pprint_binary_tree(l)

pprint_structure(l)


'''

            70
        /        \
     31         93
    /            /    \
14            73     94
    \
     23

'''
