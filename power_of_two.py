import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = False
        if n > 0:
            logged = math.log2(n)
            result = logged == math.floor(logged)
        return result
