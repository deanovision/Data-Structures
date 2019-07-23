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
        self.tail = None
        self.head = None

    def enqueue(self, item):
        self.storage.append(item)
        self.increment()
        # if self.head is None and self.tail is None:
        #     self.head = Node(item)
        #     self.tail = Node(item)
        #     self.increment()
        #     print(self.size)
        # elif self.size == 1:
        #     print(self.head.value)
        #     self.head.next_node = Node(item)
        #     print(self.head.next_node.value)
        #     self.tail = Node(item)
        #     print(self.tail.value)
        #     self.increment()
        # else:
        #     print(self.size)
        #     self.tail.next_node = Node(item)
        #     self.tail = Node(item)
        #     self.increment()

    def dequeue(self):
        if self.size > 0:
            item = self.storage.pop(0)
            self.decrement()
            return item
        # if self.head is None:
        #     print('queue is currently empty')
        # elif self.size == 1:
        #     old_head = self.head
        #     self.head = None
        #     self.tail = None
        #     self.decrement()
        #     return old_head.value
        # else:
        #     print(self.head.value)
        #     old_head = self.head
        #     new_head = self.head.next_node
        #     self.head = new_head
        #     print(self.head.value)
        #     self.decrement()
        #     return old_head.value

    def len(self):
        return self.size

    def increment(self):
        self.size += 1

    def decrement(self):
        if self.size >= 0:
            self.size -= 1
