from make_sum_divisible_by_p import Solution

def test_ex1():
    nums = [3,1,4,2]
    p = 6
    solution = Solution()
    result = solution.minSubarray(nums, p)
    assert result == 1

def test_ex2():
    nums = [6,3,5,2]
    p = 9
    solution = Solution()
    result = solution.minSubarray(nums, p)
    assert result == 2

def test_ex3():
    nums = [1,2,3]
    p = 3
    solution = Solution()
    result = solution.minSubarray(nums, p)
    assert result == 0

def test_ex4():
    nums = [1,2,3]
    p = 7
    solution = Solution()
    result = solution.minSubarray(nums, p)
    assert result == -1
