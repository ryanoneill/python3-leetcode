from bitwise_and_of_numbers_range import Solution

def test_ex1():
    left = 5
    right = 7
    solution = Solution()
    result = solution.rangeBitwiseAnd(left, right)
    assert result == 4

def test_ex2():
    left = 0
    right = 0
    solution = Solution()
    result = solution.rangeBitwiseAnd(left, right)
    assert result == 0

def test_ex3():
    left = 1
    right = 2147483647
    solution = Solution()
    result = solution.rangeBitwiseAnd(left, right)
    assert result == 0

def test_ex4():
    left = 600000000
    right = 2147483645
    solution = Solution()
    result = solution.rangeBitwiseAnd(left, right)
    assert result == 0
