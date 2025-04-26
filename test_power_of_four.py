from power_of_four import Solution

def test_ex1():
    n = 16
    solution = Solution()
    result = solution.isPowerOfFour(n)
    assert result

def test_ex2():
    n = 5
    solution = Solution()
    result = solution.isPowerOfFour(n)
    assert not result

def test_ex3():
    n = 1
    solution = Solution()
    result = solution.isPowerOfFour(n)
    assert result
