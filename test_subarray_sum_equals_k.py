from subarray_sum_equals_k import Solution

def test_ex1():
    nums = [1,1,1]
    k = 2
    solution = Solution()
    result = solution.subarraySum(nums, k)
    assert result == 2

def test_ex2():
    nums = [1,2,3]
    k = 3
    solution = Solution()
    result = solution.subarraySum(nums, k)
    assert result == 2

def test_ex3():
    nums = [-1,-1,1]
    k = 0
    solution = Solution()
    result = solution.subarraySum(nums, k)
    assert result == 1
