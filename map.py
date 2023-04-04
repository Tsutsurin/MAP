class node():

    def __init__(self, key, data):
        self.left = self.right = None
        self.key = key
        self.data = data

    def add(self, key, data):
        if key == self.key:
            self.data = data
        elif key < self.key:
            if self.left is None:
                self.left = node(key, data)
            else:
                self.left.add(key, data)
        else:
            if self.right is None:
                self.right = node(key, data)
            else:
                self.right.add(key, data)

    def delete(self, key):
        if self == None:
            return self
        if key < self.key:
            if self.left:
                self.left = self.left.delete(key)
            return self
        if key > self.key:
            if self.right:
                self.right = self.right.delete(key)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right

        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.key = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def get(self, key):
        if key == self.key:
            return self.key, self.data

        if key < self.key:
            if self.left == None:
                return "Такого ключа не существует"
            return self.left.get(key)

        if self.right == None:
            return "Такого ключа не существует"
        return self.right.get(key)

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.key

    def clear(self):
        max_el = node.get_max(self)
        for _ in range(0, max_el + 1):
            node.delete(self, _)