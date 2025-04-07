from make_the_prefix_sum_non_negative import Solution


def test_ex1():
    nums = [2, 3, -5, 4]
    solution = Solution()
    result = solution.makePrefSumNonNegative(nums)
    assert result == 0


def test_ex2():
    nums = [3, -5, -2, 6]
    solution = Solution()
    result = solution.makePrefSumNonNegative(nums)
    assert result == 1


def test_ex3():
    nums = [6, -6, -3, 3, 1, 5, -4, -3, -2, -3, 4, -1, 4, 4, -2, 6, 0]
    solution = Solution()
    result = solution.makePrefSumNonNegative(nums)
    assert result == 1
