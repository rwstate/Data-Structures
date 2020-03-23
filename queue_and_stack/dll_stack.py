import sys
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()
    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if len(self.storage):
            popped = self.storage.tail.value
            self.storage.remove_from_tail()
            return popped
        return
    def len(self):
        return len(self.storage)
