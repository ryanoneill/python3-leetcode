from maximum_average_subarray_i import Solution


def test_ex1():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    solution = Solution()
    result = solution.findMaxAverage(nums, k)
    assert result == 12.75


def test_ex2():
    nums = [5]
    k = 1
    solution = Solution()
    result = solution.findMaxAverage(nums, k)
    assert result == 5
