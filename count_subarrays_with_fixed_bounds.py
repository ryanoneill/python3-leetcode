from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0

        last_breaker = -1
        left = 0
        min_count = 0
        max_count = 0

        for right, num in enumerate(nums):
            if num < minK or num > maxK:
                last_breaker = right 
                left = right + 1
                min_count = 0
                max_count = 0
            if num == minK:
                min_count += 1
            if num == maxK:
                max_count += 1

            while min_count >= 1 and max_count >= 1:
                if left == right:
                    break
                else:
                    left_num = nums[left]
                    if left_num == minK:
                        if min_count == 1:
                            break
                        else:
                            min_count -= 1
                            left += 1
                            if left_num == maxK:
                                max_count -= 1
                    elif left_num == maxK:
                        if max_count == 1:
                            break
                        else:
                            max_count -= 1
                            left += 1
                    else:
                        left += 1

            if min_count >= 1 and max_count >= 1:
                value = left - last_breaker
                result += value


        return result 
