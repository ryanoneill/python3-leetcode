from distinct_subsequences import Solution

def test_ex1():
    s = "rabbbit"
    t = "rabbit"
    solution = Solution()
    result = solution.numDistinct(s, t)
    assert result == 3

def test_ex2():
    s = "babgbag"
    t = "bag"
    solution = Solution()
    result = solution.numDistinct(s, t)
    assert result == 5
