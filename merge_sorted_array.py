from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index1 = m - 1
        index2 = n - 1

        rindex = (m + n) - 1
        while index1 >= 0 or index2 >= 0:
            if index1 >= 0 and index2 >= 0:
                num1 = nums1[index1]
                num2 = nums2[index2]
                if num1 > num2:
                    nums1[rindex] = num1
                    index1 -= 1
                else:
                    nums1[rindex] = num2
                    index2 -= 1
            elif index1 >= 0:
                num1 = nums1[index1]
                nums1[rindex] = num1
                index1 -= 1
            else:
                num2 = nums2[index2]
                nums1[rindex] = num2
                index2 -= 1

            rindex -= 1
