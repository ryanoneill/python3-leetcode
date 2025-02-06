from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prods = {}
        result = 0
        n = len(nums)
        if n >= 4:
            for i in range(n-1):
                for j in range(i+1,n):
                    prod = nums[i] * nums[j]
                    if prod in prods:
                        prods[prod] += 1
                    else:
                        prods[prod] = 1

            for key, value in prods.items():
                if value > 1:
                    result += (value - 1) * value * 4

        return result

