class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 :
            raise ValueError("You can't have negative capacity")
        self.capacity = capacity
        self.size = 0
    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError
        self.size += n


    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

