# coding=utf-8
"""
You have two numbers represented by a linked list, where each node contains
a sin- gle digit. The digits are stored in reverse order, such that the 1’s
digit is at the head of the list. Write a function that adds the two numbers
and returns the sum as a linked list.
"""


class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.last = None

    def add(self, value):
        if not self.next:
            self.next = LinkedList(value)
            self.last = self.next
        else:
            self.last.next = LinkedList(value)
            self.last = self.last.next

    def print_linked_list(self):
        if self.next:
            print("{} ->".format(self.value)),
            self.next.print_linked_list()
        else:
            print("{}".format(self.value))

    def get_numbers(self):
        numbers = ''
        while self.next:
            numbers += str(self.value)
            self = self.next
        numbers += str(self.value)
        return int(numbers[::-1])


if __name__ == '__main__':
    first_number = LinkedList(3)
    first_number.add(1)
    first_number.add(5)
    first_number.print_linked_list()

    second_number = LinkedList(5)
    second_number.add(9)
    second_number.add(2)
    second_number.print_linked_list()

    print first_number.get_numbers() + second_number.get_numbers()
