class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        results = [0] * 50
        results[0] = 5
        results[1] = 20
        for i in range(2, 50):
            result = results[i - 1]
            result *= result
            result = result % MOD
            results[i] = result

        result = 0
        for i in reversed(range(50)):
            value = 2**i
            while n >= value:
                if result == 0:
                    result = results[i]
                else:
                    result *= results[i]
                    result = result % MOD
                n -= value

        return result
