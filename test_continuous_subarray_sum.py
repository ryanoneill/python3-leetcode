from continuous_subarray_sum import Solution

def test_ex1():
    nums = [23,2,4,6,7]
    k = 6
    solution = Solution()
    result = solution.checkSubarraySum(nums, k)
    assert result

def test_ex2():
    nums = [23,2,6,4,7]
    k = 6
    solution = Solution()
    result = solution.checkSubarraySum(nums, k)
    assert result

def test_ex3():
    nums = [23,2,6,4,7]
    k = 13
    solution = Solution()
    result = solution.checkSubarraySum(nums, k)
    assert not result

def test_ex4():
    nums = [0]
    k = 1
    solution = Solution()
    result = solution.checkSubarraySum(nums, k)
    assert not result

def test_ex5():
    nums = [23,2,4,6,6]
    k = 7
    solution = Solution()
    result = solution.checkSubarraySum(nums, k)
    assert result
