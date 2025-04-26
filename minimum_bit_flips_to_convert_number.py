import itertools

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bits = list(reversed(bin(start)[2:]))
        goal_bits = list(reversed(bin(goal)[2:]))

        result = 0
        for start_bit, goal_bit in itertools.zip_longest(start_bits, goal_bits):
            if start_bit is None:
                if goal_bit == "1":
                    result += 1 
            elif goal_bit is None:
                if start_bit == "1":
                    result += 1
            elif start_bit != goal_bit:
                result += 1

        return result
