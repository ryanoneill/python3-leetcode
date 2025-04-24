from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique = len(set(nums))

        result = 0
        left = 0
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
            current = len(counts)
            if current == unique:
                while True:
                    previous = nums[left]
                    if counts[previous] > 1:
                        counts[previous] -= 1
                        left += 1
                    else:
                        break
                result += left + 1

        return result 
