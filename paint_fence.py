class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        elif n == 2:
            return k * k
        else:
            two_away = k
            one_away = k * k

            result = 0
            for _ in range(3, n+1):
                result = (k - 1) * (two_away + one_away)
                two_away = one_away
                one_away = result

            return result
