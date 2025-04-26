from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0

        last = -1
        count = 0
        left = 0
        for right, num in enumerate(nums):
            if num == 1:
                count += 1
            while count >= goal:
                if left == right:
                    break
                else:
                    left_num = nums[left]
                    if left_num == 1:
                        if count > goal:
                            last = left
                            count -= 1
                            left += 1
                        else:
                            break
                    else:
                        left += 1
            if count == goal:
                result += left - last

        return result


