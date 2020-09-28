class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # max amount
        self.buffer = []  # created list
        self.i = 0  # 0 set as initial index

    """append an element at the end of the buffer"""

    def append(self, item):
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        else:
            self.buffer[self.i] = item
            if self.i == self.capacity - 1:
                self.i = (self.i + 1) % self.capacity  # overides the oldest element in list
            else:
                self.i += 1  # increment by 1

    """ Return a list of elements from the oldest to the newest. """

    def get(self):
        return self.buffer
