from unique_paths import Solution

def test_ex1():
    m = 3
    n = 7
    solution = Solution()
    result = solution.uniquePaths(m, n)
    assert result == 28

def test_ex2():
    m = 3
    n = 2
    solution = Solution()
    result = solution.uniquePaths(m, n)
    assert result == 3
