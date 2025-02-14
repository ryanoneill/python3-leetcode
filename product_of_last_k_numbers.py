import math

class ProductOfNumbers:
    def __init__(self):
        self.items = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.items = [1]
            self.size = 0
        else:
            self.items.append(self.items[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        result = 0
        if k <= self.size:
            result = self.items[self.size] // self.items[self.size - k]
        return result
