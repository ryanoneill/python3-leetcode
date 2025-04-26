from ways_to_split_array_into_good_subarrays import Solution

def test_ex1():
    nums = [0,1,0,0,1]
    solution = Solution()
    result = solution.numberOfGoodSubarraySplits(nums)
    assert result == 3

def test_ex2():
    nums = [0,1,0]
    solution = Solution()
    result = solution.numberOfGoodSubarraySplits(nums)
    assert result == 1

def test_ex3():
    nums = [0,1,0,0,1,0,1]
    solution = Solution()
    result = solution.numberOfGoodSubarraySplits(nums)
    assert result == 6

def test_ex4():
    nums = [0,0]
    solution = Solution()
    result = solution.numberOfGoodSubarraySplits(nums)
    assert result == 0
