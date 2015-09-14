'''
Implementing a linked list
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def append_to_tail(self, el):
        self.next = el

    def print_association(self):
        print '%s -> %s' % (self.data, self.next)


a = Node('a')
a.append_to_tail('b')

b = Node('b')
b.append_to_tail('c')

a.print_association()
b.print_association()
