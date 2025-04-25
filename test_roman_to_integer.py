from roman_to_integer import Solution


def test_ex1():
    s = "III"
    solution = Solution()
    result = solution.romanToInt(s)
    assert result == 3


def test_ex2():
    s = "LVIII"
    solution = Solution()
    result = solution.romanToInt(s)
    assert result == 58


def test_ex3():
    s = "MCMXCIV"
    solution = Solution()
    result = solution.romanToInt(s)
    assert result == 1994
