from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        m = len(nums1)
        n = len(nums2)

        xor1 = 0
        xor2 = 0

        if m % 2 == 1:
            xor2 = nums2[0]
            for i in range(1,n):
                xor2 ^= nums2[i]

        if n % 2 == 1:
            xor1 = nums1[0]
            for i in range(1,m):
                xor1 ^= nums1[i]

        if m % 2 == 1 and n % 2 == 1:
            result = xor2 ^ xor1
        elif m % 2 == 1:
            result = xor2
        elif n % 2 == 1:
            result = xor1
        else:
            result = 0

        return result
