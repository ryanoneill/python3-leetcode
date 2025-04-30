from maximum_sum_circular_subarray import Solution

def test_ex1():
    nums = [1,-2,3,-2]
    solution = Solution()
    result = solution.maxSubarraySumCircular(nums)
    assert result == 3

def test_ex2():
    nums = [5,-3,5]
    solution = Solution()
    result = solution.maxSubarraySumCircular(nums)
    assert result == 10

def test_ex3():
    nums = [-3,-2,-3]
    solution = Solution()
    result = solution.maxSubarraySumCircular(nums)
    assert result == -2
