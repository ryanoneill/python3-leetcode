from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        found = set()
        expected = 0
        actual = 0
        result = 0

        for i in range(len(nums)):
            expected += i + 1
            num = nums[i]
            if num not in found:
                actual += num
                found.add(num)
            else:
                result = num

        return [result, expected - actual]
