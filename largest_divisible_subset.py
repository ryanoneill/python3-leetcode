from typing import List


class Solution(object):
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        subsets = {}

        for num in nums:
            result = {}
            for key in subsets.keys():
                if num % key == 0:
                    value = subsets[key]
                    if len(value) > len(result):
                        result = value

            result = set(result)
            result.add(num)
            subsets[num] = result

        return sorted(list(max(subsets.values(), key=len)))
