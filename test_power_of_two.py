from power_of_two import Solution

def test_ex1():
    n = 1
    solution = Solution()
    result = solution.isPowerOfTwo(n)
    assert result

def test_ex2():
    n = 16
    solution = Solution()
    result = solution.isPowerOfTwo(n)
    assert result

def test_ex3():
    n = 3
    solution = Solution()
    result = solution.isPowerOfTwo(n)
    assert not result
