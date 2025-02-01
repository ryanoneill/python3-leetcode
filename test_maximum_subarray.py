from maximum_subarray import Solution

def test_ex1():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    result = solution.maxSubArray(nums)
    assert result == 6

def test_ex2():
    nums = [1]
    solution = Solution()
    result = solution.maxSubArray(nums)
    assert result == 1

def test_ex3():
    nums = [5,4,-1,7,8]
    solution = Solution()
    result = solution.maxSubArray(nums)
    assert result == 23

def test_ex4():
    nums = [-1]
    solution = Solution()
    result = solution.maxSubArray(nums)
    assert result == -1
