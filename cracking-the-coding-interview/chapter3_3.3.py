"""
Imagine a (literal) stack of plates. If the stack gets too high, it might
topple. Therefore, in real life, we would likely start a new stack when
the previous stack exceeds some threshold. Implement a data structure
SetOfStacks that mimics this. SetOfStacks should be composed of several
stacks, and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a
single stack (that is, pop() should return the same values as it would if
there were just a single stack).

FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a
specific sub-stack.
"""


class SetOfStacks(object):
    def __init__(self, threshold):
        self.current_stack = 0
        self.stacks = [[]]
        self.threshold = int(threshold)

    def push(self, element):
        if isinstance(element, list):
            for el in element:
                if self.threshold == len(self.stacks[self.current_stack]):
                    self.current_stack += 1
                    self.stacks.append([])
                    self.stacks[self.current_stack].append(el)
                else:
                    self.stacks[self.current_stack].append(el)
        else:
            if self.threshold == len(self.stacks[self.current_stack]):
                self.current_stack += 1
                self.stacks.append([])
                self.stacks[self.current_stack].append(element)
            else:
                self.stacks[self.current_stack].append(element)

    def pop(self):
        return self.stacks[self.current_stack].pop()

    def pop_at_index(self, index):
        return self.stacks[index].pop()

    def print_stack(self):
        for i, stack in enumerate(self.stacks):
            print '%d : %s' % (i + 1, stack)

    def __repr__(self):
        return str(self.stacks)
