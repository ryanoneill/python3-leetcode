from typing import List

class Solution:
    def factorial(self, n: int) -> List[int]:
        result = [0] * (n+1)
        result[0] = 1
        result[1] = 1
        for i in range(2, n+1):
            result[i] = result[i-1] * i

        return result

    def countGoodIntegers(self, n: int, k: int) -> int:
        result = 0
        good = set()

        # Even
        # m = n / 2
        # 9 * 10^m-1
        # Odd
        # m = (n - 1) / 2
        # 9 * 10^m

        mid = 0
        count = 0
        if n % 2 == 0:
            mid = n // 2
            count = mid - 1
        else:
            mid = (n - 1) // 2
            count = mid
        part_mult = 10**count

        for start in range(1, 9+1):
            begin = start
            begin *= part_mult
            for i in range(0, part_mult):
                part = begin
                part += i

                part_s = str(part)
                if n % 2 == 0:
                    full_s = part_s + part_s[::-1]
                else:
                    full_s = part_s + part_s[::-1][1:]

                full = int(full_s)
                if full % k == 0:
                    good.add("".join(sorted(full_s)))

        # TOO SLOW
        # for start in range(1, 9+1):
        #     begin = start
        #     begin *= full_mult
        #     for i in range(0, full_mult):
        #         num = begin
        #         num += i
        #         key = "".join(sorted(str(num)))
        #         if key in good:
        #             result += 1

        # Couldn't remember how to calculate this number using
        # Combinatorics. This section is from the editorial.
        fac = self.factorial(n)
        for s in good:
            cnt = [0] * 10
            for c in s:
                cnt[int(c)] += 1
            # Calculate permutations and combinations
            tot = (n - cnt[0]) * fac[n - 1]
            for x in cnt:
                tot //= fac[x]
            result += tot

        return result
