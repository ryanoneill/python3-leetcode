from largest_substring_between_two_equal_characters import Solution

def test_ex1():
    s = "aa"
    solution = Solution()
    result = solution.maxLengthBetweenEqualCharacters(s)
    assert result == 0

def test_ex2():
    s = "abca"
    solution = Solution()
    result = solution.maxLengthBetweenEqualCharacters(s)
    assert result == 2

def test_ex3():
    s = "cbzxy"
    solution = Solution()
    result = solution.maxLengthBetweenEqualCharacters(s)
    assert result == -1
