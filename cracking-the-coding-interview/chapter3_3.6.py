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

    def __getitem__(self, indx):
        return self.stack[indx]


def quicksort(lst):
    """Qucksort."""
    if lst == []:
        return []
    else:
        pivot = lst[0]
        smaller = quicksort([x for x in lst[1:] if x < pivot])
        greater = quicksort([x for x in lst[1:] if x >= pivot])
        return smaller + [pivot] + greater


if __name__ == '__main__':
    array = [3, 7, 9, 6, 3, 3, 5, 7, 9, 0, 6, 3]
    print(' '.join([str(n) for n in array]))
    stack = Stack(array)
    sorted_stack = quicksort(stack)
    print(' '.join([str(n) for n in sorted_stack]))
