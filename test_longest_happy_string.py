from longest_happy_string import Solution

def test_ex1():
    a = 1
    b = 1
    c = 7
    solution = Solution()
    result = solution.longestDiverseString(a, b, c)
    assert result == "ccaccbcc"

def test_ex2():
    a = 7
    b = 1
    c = 0
    solution = Solution()
    result = solution.longestDiverseString(a, b, c)
    assert result == "aabaa"
