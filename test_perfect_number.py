from perfect_number import Solution

def test_ex1():
    num = 28
    solution = Solution()
    result = solution.checkPerfectNumber(num)
    assert result

def test_ex2():
    num = 7
    solution = Solution()
    result = solution.checkPerfectNumber(num)
    assert not result

def test_ex3():
    num = 99999992
    solution = Solution()
    result = solution.checkPerfectNumber(num)
    assert not result

def test_ex4():
    num = 1
    solution = Solution()
    result = solution.checkPerfectNumber(num)
    assert not result
