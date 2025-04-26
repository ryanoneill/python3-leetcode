import itertools

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bits = list(reversed(bin(x)[2:]))
        y_bits = list(reversed(bin(y)[2:]))

        result = 0
        for x_bit, y_bit in itertools.zip_longest(x_bits, y_bits):
            if x_bit is None:
                if y_bit == "1":
                    result += 1 
            elif y_bit is None:
                if x_bit == "1":
                    result += 1
            elif x_bit != y_bit:
                result += 1

        return result
