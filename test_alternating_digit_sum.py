from alternating_digit_sum import Solution

def test_ex1():
    n = 521
    solution = Solution()
    result = solution.alternateDigitSum(n)
    assert result == 4

def test_ex2():
    n = 111
    solution = Solution()
    result = solution.alternateDigitSum(n)
    assert result == 1

def test_ex3():
    n = 886996
    solution = Solution()
    result = solution.alternateDigitSum(n)
    assert result == 0
