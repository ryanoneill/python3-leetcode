class Solution:
    def largestOddNumber(self, num: str) -> str:
        result = ""
        n = len(num)
        for i in reversed(range(n)):
            if int(num[i]) % 2 == 1:
                result = num[:i+1]
                break

        return result
