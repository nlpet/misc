"""
Write a program to sort a stack in ascending order. You should not
make any assump- tions about how the stack is implemented. The
following are the only functions that should be used to write this
program: push | pop | peek | isEmpty.
"""


class Stack(object):
    def __init__(self, stack):
        assert isinstance(stack, list) == True, "Stack should be a list."
        self.stack = stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.pop()

    def peek(self):
        return self.stack[0]

    def is_empty(self):
        return len(self.stack) == 0

    def sort(self):
        """Qucksort."""
        if self.stack == []:
            return []
        else:
            pivot = self.stack[0]
            smaller = self.sort([x for x in self.stack[1:] if x < pivot])
            greater = self.sort([x for x in self.stack[1:] if x >= pivot])
            return smaller + [pivot] + greater


if __name__ == '__main__':
    array = [3,7,9,6,3,3,5,7,9,0,6,3]
    print ' '.join([str(n) for n in array])
    stack = Stack(array)
    sorted_stack =  stack.sort()
    print ' '.join([str(n) for n in sorted_stack])
