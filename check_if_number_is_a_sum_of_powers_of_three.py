class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        result = True
        while n > 0:
            if n % 3 == 2:
                result = False
                break
            n //= 3
        return result
