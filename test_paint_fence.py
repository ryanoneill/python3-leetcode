from paint_fence import Solution

def test_ex1():
    n = 3
    k = 2
    solution = Solution()
    result = solution.numWays(n, k)
    assert result == 6

def test_ex2():
    n = 1
    k = 1
    solution = Solution()
    result = solution.numWays(n, k)
    assert result == 1

def test_ex3():
    n = 7
    k = 2
    solution = Solution()
    result = solution.numWays(n, k)
    assert result == 42
