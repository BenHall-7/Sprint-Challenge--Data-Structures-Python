class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.oldest = 0
        self.capacity = capacity

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.oldest] = item
            self.oldest = (self.oldest + 1) % self.capacity
        else:
            self.storage.append(item)

    def get(self):
        return self.storage