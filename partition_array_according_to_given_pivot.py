from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = 0
        equal = 0
        larger = 0

        for num in nums:
            if num < pivot:
                smaller += 1
            elif num > pivot:
                larger += 1
            else:
                equal += 1

        n = len(nums)
        results = [0 for _ in range(n)]
        s_index = 0
        e_index = smaller
        l_index = smaller + equal

        for num in nums:
            if num < pivot:
                results[s_index] = num
                s_index += 1
            elif num > pivot:
                results[l_index] = num
                l_index += 1
            else:
                results[e_index] = num
                e_index += 1

        return results
