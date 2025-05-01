class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        result = 0

        a, e, i, o, u = 0, 1, 2, 3, 4

        previous = [1,1,1,1,1]
        current = [0,0,0,0,0]

        for _ in range(2, n+1):
            current[a] = (previous[e]) % MOD
            current[e] = (previous[a] + previous[i]) % MOD
            current[i] = (previous[a] + previous[e] + previous[o] + previous[u]) % MOD
            current[o] = (previous[i] + previous[u]) % MOD
            current[u] = (previous[a]) % MOD

            previous, current = current, previous


        result = sum(previous) % MOD
        return result

