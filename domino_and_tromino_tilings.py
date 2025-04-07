class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007
        result = 0

        if n <= 2:
            result = n
        else:
            partial = 1
            full = 2
            full_prev = 1

            for _ in range(3, n + 1):
                new_partial = (partial + full_prev) % MOD
                new_full = (full + full_prev + 2 * partial) % MOD

                result = new_full
                full_prev = full
                full = new_full
                partial = new_partial

        return result
