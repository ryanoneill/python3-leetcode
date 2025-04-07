from partition_equal_subset_sum import Solution


def test_ex1():
    nums = [1, 5, 11, 5]
    solution = Solution()
    result = solution.canPartition(nums)
    assert result


def test_ex2():
    nums = [1, 2, 3, 5]
    solution = Solution()
    result = solution.canPartition(nums)
    assert not result


def test_ex3():
    nums = [1, 2, 5]
    solution = Solution()
    result = solution.canPartition(nums)
    assert not result
