from fenwick_tree import FenwickTree
from typing import List, Dict


class Solution:
    def indexed(self, nums: List[int]) -> Dict[int, int]:
        result = {}
        for i, num in enumerate(nums):
            result[num] = i
        return result

    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0

        n = len(nums1)
        nums1indexed = self.indexed(nums1)
        tree = FenwickTree(n)

        for i, num in enumerate(nums2):
            nums1index = nums1indexed[num]
            left = tree.prefix(nums1index)
            tree.update(nums1index, 1)
            right = (n - 1 - nums1index) - (i - left)
            result += left * right

        return result
