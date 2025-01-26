from queue import deque

class MovingAverage:

    def __init__(self, size: int):
        self.values = deque()
        self.count = 0
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        if self.count == self.size:
            previous = self.values.popleft()
            self.total -= previous
            self.count -= 1

        self.total += val
        self.count += 1
        self.values.append(val)

        return self.total / self.count
