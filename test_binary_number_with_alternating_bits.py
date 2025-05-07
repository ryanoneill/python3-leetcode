from binary_number_with_alternating_bits import Solution

def test_ex1():
    n = 5
    solution = Solution()
    result = solution.hasAlternatingBits(n)
    assert result

def test_ex2():
    n = 7
    solution = Solution()
    result = solution.hasAlternatingBits(n)
    assert not result

def test_ex3():
    n = 11
    solution = Solution()
    result = solution.hasAlternatingBits(n)
    assert not result
