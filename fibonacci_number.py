class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            two_away = 0
            one_away = 1

            result = 0
            for _ in range(2, n+1):
                result = one_away + two_away
                two_away = one_away
                one_away = result

            return result

