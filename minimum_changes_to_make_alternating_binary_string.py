class Solution:
    def minOperations(self, s: str) -> int:
        one = 0
        for i, digit in enumerate(s):
            if i % 2 == 0:
                if digit != "1":
                    one += 1
            elif digit != "0":
                one += 1

        return min(one, len(s) - one)
