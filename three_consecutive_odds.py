from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        result = False

        minus_one = False
        minus_two = False
        
        for num in arr:
            is_odd = num % 2 == 1
            result = is_odd and minus_one and minus_two
            if result:
                break
            else:
                minus_two = minus_one
                minus_one = is_odd

        return result

