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

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def pre_order(self):
        if self:
            print_node(str(self.value))
            if self.left:
                self.left.pre_order()
            if self.right:
                self.right.pre_order()

    def post_order(self):
        if self:
            if self.left:
                self.left.post_order()
            if self.right:
                self.right.post_order()
            print_node(str(self.value))

    def in_order(self):
        if self:
            if self.left:
                self.left.in_order()
            if self.right:
                self.right.in_order()
            print_node(str(self.value))

    def __repr__(self):
        return "%s : %s" % (self.__class__, self.value)

    def __str__(self):
        return str(self.value)

    def print_node(self):
        print("Root: {}".format(self.value))
        print("Left: {}".format(self.left))
        print("Right: {}".format(self.right))


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def pre_order(self):
        print("Pre-order traversal")
        self.root.pre_order()
        print("")

    def post_order(self):
        print("Post-order traversal")
        self.root.post_order()
        print("")

    def in_order(self):
        print("In-order traversal")
        self.root.in_order()
        print("")

    def __repr__(self):
        return "%s : %s" % (self.__class__, self.root)

    def print_tree(self):
        if self:
            self.root.print_node()



def print_node(value):
    print(value, end=" ")


if __name__ == '__main__':
    tree = Tree()
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(6)
    tree.insert(4)
    tree.insert(2)
    # tree.pre_order()
    tree.print_tree()
