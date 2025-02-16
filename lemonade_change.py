from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        result = True
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives > 0:
                    fives -= 1
                    tens += 1
                else:
                    result = False
                    break
            else:
                if fives == 0:
                    result = False
                    break
                elif tens > 0:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    result = False
                    break
        return result
