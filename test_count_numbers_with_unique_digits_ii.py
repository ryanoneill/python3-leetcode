from count_numbers_with_unique_digits_ii import Solution

def test_ex1():
    a = 1
    b = 20
    solution = Solution()
    result = solution.numberCount(a, b)
    assert result == 19

def test_ex2():
    a = 9
    b = 19
    solution = Solution()
    result = solution.numberCount(a, b)
    assert result == 10 

def test_ex3():
    a = 80
    b = 120
    solution = Solution()
    result = solution.numberCount(a, b)
    assert result == 27
