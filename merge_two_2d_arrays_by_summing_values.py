from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        results = []
        nums1_i = 0
        nums2_i = 0

        nums1_n = len(nums1)
        nums2_n = len(nums2)

        while nums1_i < nums1_n or nums2_i < nums2_n: 
            if nums1_i < nums1_n and nums2_i < nums2_n:
                nums1_value = nums1[nums1_i]
                nums2_value = nums2[nums2_i]

                if nums1_value[0] == nums2_value[0]:
                    key = nums1_value[0]
                    sum = nums1_value[1] + nums2_value[1]
                    results.append([key, sum])
                    nums1_i += 1
                    nums2_i += 1
                elif nums1_value[0] < nums2_value[0]:
                    results.append(nums1_value)
                    nums1_i += 1
                else:
                    results.append(nums2_value)
                    nums2_i += 1
            elif nums1_i < nums1_n:
                nums1_value = nums1[nums1_i]
                results.append(nums1_value)
                nums1_i += 1
            else:
                nums2_value = nums2[nums2_i]
                results.append(nums2_value)
                nums2_i += 1

        return results
