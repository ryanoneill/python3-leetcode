class FenwickTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (n + 1) # 1-indexed

    def update(self, index, delta):
        index += 1
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def prefix(self, index):
        index = min(index +1, self.n)

        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index

        return result

    def range(self, left, right):
        result = self.prefix(right)
        if left > 0:
            result -= self.prefix(left-1)

    def value(self, index):
        return self.range(index, index)
