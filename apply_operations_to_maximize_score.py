from typing import List


class Solution:
    def _power(self, base: int, exponent: int) -> int:
        MOD = 10**9 + 7

        result = 1

        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % MOD

            base = (base * base) % MOD
            exponent //= 2

        return result

    def primes(self, n: int) -> List[int]:
        result = []
        values = [True] * (n + 1)
        if n >= 2:
            values[0] = False
            values[1] = False

            for i in range(2, n + 1):
                if values[i]:
                    result.append(i)
                    for j in range(i * i, n + 1, i):
                        values[j] = False

        return result

    def prime_scores(self, nums: List[int]) -> List[int]:
        max_value = max(nums)
        primes = self.primes(max_value)

        n = len(nums)
        result = [0] * n

        for index in range(n):
            num = nums[index]

            for prime in primes:
                if prime * prime > num:
                    break
                if num % prime == 0:
                    result[index] += 1
                    while num % prime == 0:
                        num //= prime

            if num > 1:
                result[index] += 1

        return result

    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        prime_scores = self.prime_scores(nums)
        left = [-1 for _ in range(n)]
        right = [n for _ in range(n)]

        stack = []
        for index in range(n):
            if stack:
                while stack and prime_scores[index] > prime_scores[stack[-1]]:
                    previous = stack.pop()
                    right[previous] = index
                if stack:
                    left[index] = stack[-1]
            stack.append(index)

        ordered = sorted(enumerate(nums), key=lambda value: -value[1])
        result = 1

        i = 0
        while k > 0:
            index, num = ordered[i]
            count = (index - left[index]) * (right[index] - index)
            times = min(k, count)
            result = result * self._power(num, times) % MOD
            k -= times
            i += 1

        return result
