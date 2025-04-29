class Solution:
    def numDecodings(self, s: str) -> int:
        result = 0

        two_away = 0
        one_away = 1
        
        previous = -1
        for letter in s:
            result = 0
            digit = int(letter)
            if digit != 0:
                result += one_away
            if previous == 1:
                result += two_away
            elif previous == 2 and digit <= 6:
                result += two_away
            previous = digit
            two_away = one_away
            one_away = result

        return result
