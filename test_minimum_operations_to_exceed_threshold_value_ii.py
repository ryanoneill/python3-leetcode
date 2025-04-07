from minimum_operations_to_exceed_threshold_value_ii import Solution


def test_ex1():
    nums = [2, 11, 10, 1, 3]
    k = 10
    solution = Solution()
    result = solution.minOperations(nums, k)
    assert result == 2


def test_ex2():
    nums = [1, 1, 2, 4, 9]
    k = 20
    solution = Solution()
    result = solution.minOperations(nums, k)
    assert result == 4
