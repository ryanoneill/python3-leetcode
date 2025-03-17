from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = sorted(nums, key=lambda num: (counter[num], -num))
        return result
        
