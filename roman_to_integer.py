class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        n = len(s)
        result = 0
        index = 0
        while index < n:
            if index < n-1 and s[index:index+2] in map:
                result += map[s[index:index+2]]
                index += 2
            else:
                result += map[s[index]]
                index += 1
        return result
