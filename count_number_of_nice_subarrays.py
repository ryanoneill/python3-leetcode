from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = 0

        left = 0
        last = -1
        count = 0
        for num in nums:
            if num % 2 == 1:
                count += 1
            while count >= k:
                left_num = nums[left]
                is_odd = left_num % 2 == 1
                if not is_odd:
                    left += 1
                elif count == k:
                    break
                else:
                    last = left
                    left += 1
                    count -= 1
            if count == k:
                result += left - last

        return result
