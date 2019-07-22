class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_value(self, value):
        self.value = value

    def update_next(self, new_next_node):
        self.next_node = new_next_node


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
        self.increment()

    def dequeue(self):
        self.storage.pop(0)
        self.decrement()

    def len(self):
        pass

    def increment(self):
        self.size += 1

    def decrement(self):
        if self.size >= 0:
            self.size -= 1
