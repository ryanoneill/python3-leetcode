class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        previous = [0] * 26
        current = [0] * 26

        for letter in s:
            index = ord(letter) - ord("a")
            current[index] += 1

        for _ in range(t):
            previous, current = current, previous
            current[0] = 0
            for i in range(0, 25):
                current[i+1] = previous[i] % MOD
            if previous[25] > 0:
                current[0] += previous[25]
                current[1] += previous[25]

        result = sum(current) % MOD
        return result
