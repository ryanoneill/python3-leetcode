import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        if str1 + str2 == str2 + str1:
            n = math.gcd(len(str1), len(str2))
            result = str1[:n]
        
        return result
