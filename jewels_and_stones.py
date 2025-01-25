class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        result = 0
        for letter in stones:
            if letter in jewels:
                result += 1
        return result
