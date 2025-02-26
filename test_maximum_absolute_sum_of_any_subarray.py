from maximum_absolute_sum_of_any_subarray import Solution

def test_ex1():
    nums = [1,-3,2,3,-4]
    solution = Solution()
    result = solution.maxAbsoluteSum(nums)
    assert result == 5

def test_ex2():
    nums = [2,-5,1,-4,3,-2]
    solution = Solution()
    result = solution.maxAbsoluteSum(nums)
    assert result == 8
