from ugly_number import Solution

def test_ex1():
    n = 6
    solution = Solution()
    result = solution.isUgly(n)
    assert result

def test_ex2():
    n = 1
    solution = Solution()
    result = solution.isUgly(n)
    assert result

def test_ex3():
    n = 14
    solution = Solution()
    result = solution.isUgly(n)
    assert not result
