class Solution:
    def isUgly(self, n: int) -> bool:
        result = True
        if n <= 0:
            result = False
        else:
            while n > 1:
                if n % 5 == 0:
                    n //= 5
                elif n % 3 == 0:
                    n //= 3
                elif n % 2 == 0:
                    n //= 2
                else:
                    result = False
                    break

        return result

