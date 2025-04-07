from find_the_distinct_difference_array import Solution


def test_ex1():
    nums = [1, 2, 3, 4, 5]
    solution = Solution()
    result = solution.distinctDifferenceArray(nums)
    assert result == [-3, -1, 1, 3, 5]
