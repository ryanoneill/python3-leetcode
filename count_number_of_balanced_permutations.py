from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        cache = {}
        def worker(digit: int, sum_left: int, odds_left: int, evens_left: int) -> int:
            result = 0
            if digit > 9:
                if sum_left == 0 and odds_left == 0 and evens_left == 0:
                    result = 1
            elif odds_left == 0 and sum_left > 0:
                result = 0
            else:
                key = (digit, sum_left, odds_left, evens_left)
                if key not in cache:
                    result = 0
                    digit_count = counts[digit]
                    for odd_count in range(min(digit_count, odds_left) + 1):
                        even_count = digit_count - odd_count
                        adding = odd_count * digit
                        if 0 <= even_count <= evens_left and adding <= sum_left:
                            value = comb(odds_left, odd_count)
                            value *= comb(evens_left, even_count)
                            value *= worker(digit + 1, sum_left - adding, odds_left - odd_count, evens_left - even_count)
                            result = (result + value) % MOD
                    cache[key] = result
                result = cache[key]
            return result

        result = 0
        MOD = 10 ** 9 + 7

        n = len(num)
        nums = list(map(int, num))
        total = sum(nums)
        if total % 2 == 0:
            half = total // 2
            evens = n // 2
            odds = n - evens
            counts = Counter(nums)

            result = worker(0, half, odds, evens)

        return result
