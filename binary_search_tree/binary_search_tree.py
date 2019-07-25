class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # if not self.left and not self.right:
        #     self.left = BinarySearchTree(value)
        # if value <= self.left:
        #   self.left.insert(value)
        # else:
        #         self.left.insert(value)

        if value <= self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        # else:
        #     cb(self.value)
        #     return
