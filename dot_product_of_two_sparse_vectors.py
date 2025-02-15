from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.items = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num != 0:
                self.items[i] = num

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for key in self.items:
            if key in vec.items:
                result += self.items[key] * vec.items[key]

        return result
