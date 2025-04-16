from greatest_common_divisor_of_strings import Solution

def test_ex1():
    str1 = "ABCABC"
    str2 = "ABC"
    solution = Solution()
    result = solution.gcdOfStrings(str1, str2)
    assert result == "ABC"

def test_ex2():
    str1 = "ABABAB"
    str2 = "ABAB"
    solution = Solution()
    result = solution.gcdOfStrings(str1, str2)
    assert result == "AB"

def test_ex3():
    str1 = "LEET"
    str2 = "CODE"
    solution = Solution()
    result = solution.gcdOfStrings(str1, str2)
    assert result == ""
