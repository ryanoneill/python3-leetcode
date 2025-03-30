class Solution:
    def countPrimes(self, n: int) -> int:
        result = 0
        if n >= 3:
            primes = [True] * n
            primes[0] = False
            primes[1] = False

            for i in range(2, n):
                if primes[i]:
                    result += 1
                    for i in range(i * i, n, i):
                        primes[i] = False

        return result
