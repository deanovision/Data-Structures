class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        # if parent is smaller swap with child
        child_index = index
        parent_index = (child_index - 1) // 2
        parent_node = self.storage[parent_index]
        child_node = self.storage[child_index]
        if parent_node < child_node:
            parent_node, child_node = child_node, parent_node

    def _sift_down(self, index):
        # grabs the indices of this element's children and determines which child has a larger value.
        # If the larger child's value is larger than the parent's value,
        # the child element is swapped with the parent.
        parent_index = index
        child1_index = 2 * parent_index + 1
        child2_index = 2 * parent_index + 2
        parent_node = self.storage[parent_index]
        child1_node = self.storage[child1_index]
        child2_node = self.storage[child2_index]
        largest_child = None
        if child1_node >= child2_node:
            largest_child = child1_node
        else:
            largest_child = child2_node
        if largest_child > parent_node:
            parent_node, largest_child = largest_child, parent_node
