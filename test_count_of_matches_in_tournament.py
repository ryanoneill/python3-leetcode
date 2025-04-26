from count_of_matches_in_tournament import Solution

def test_ex1():
    n = 7
    solution = Solution()
    result = solution.numberOfMatches(n)
    assert result == 6

def test_ex2():
    n = 14
    solution = Solution()
    result = solution.numberOfMatches(n)
    assert result == 13
