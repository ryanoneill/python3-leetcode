from count_integers_with_even_digit_sum import Solution


def test_ex1():
    num = 4
    solution = Solution()
    result = solution.countEven(num)
    assert result == 2


def test_ex2():
    num = 30
    solution = Solution()
    result = solution.countEven(num)
    assert result == 14
