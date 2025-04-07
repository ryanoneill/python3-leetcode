from running_sum_of_1d_array import Solution


def test_ex1():
    nums = [1, 2, 3, 4]
    solution = Solution()
    result = solution.runningSum(nums)
    assert result == [1, 3, 6, 10]


def test_ex2():
    nums = [1, 1, 1, 1, 1]
    solution = Solution()
    result = solution.runningSum(nums)
    assert result == [1, 2, 3, 4, 5]


def test_ex3():
    nums = [3, 1, 2, 10, 1]
    solution = Solution()
    result = solution.runningSum(nums)
    assert result == [3, 4, 6, 16, 17]
