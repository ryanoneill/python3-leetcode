from typing import List

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.nums = []
        self.counts = {}
        self.unique_index = 0

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        result = -1
        n = len(self.nums)
        if self.unique_index < n:
            result = self.nums[self.unique_index]
            while self.counts[result] > 1:
                self.unique_index += 1
                if self.unique_index == n:
                    result = -1
                    break
                else:
                    result = self.nums[self.unique_index]
        return result

    def add(self, value: int) -> None:
        self.nums.append(value)
        if value in self.counts:
            self.counts[value] += 1
        else:
            self.counts[value] = 1
