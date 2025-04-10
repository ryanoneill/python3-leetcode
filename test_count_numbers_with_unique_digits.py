from count_numbers_with_unique_digits import Solution

def test_ex1():
    n = 2
    solution = Solution()
    result = solution.countNumbersWithUniqueDigits(n)
    assert result == 91

def test_ex2():
    n = 0
    solution = Solution()
    result = solution.countNumbersWithUniqueDigits(n)
    assert result == 1

def test_ex3():
    n = 1
    solution = Solution()
    result = solution.countNumbersWithUniqueDigits(n)
    assert result == 10

def test_ex4():
    n = 8
    solution = Solution()
    result = solution.countNumbersWithUniqueDigits(n)
    assert result == 2345851
