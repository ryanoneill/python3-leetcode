from maximum_ascending_subarray_sum import Solution


def test_ex1():
    nums = [10, 20, 30, 5, 10, 50]
    solution = Solution()
    result = solution.maxAscendingSum(nums)
    assert result == 65


def test_ex2():
    nums = [10, 20, 30, 40, 50]
    solution = Solution()
    result = solution.maxAscendingSum(nums)
    assert result == 150


def test_ex3():
    nums = [12, 17, 15, 13, 10, 11, 12]
    solution = Solution()
    result = solution.maxAscendingSum(nums)
    assert result == 33
