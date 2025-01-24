from max_consecutive_ones_iii import Solution

def test_ex1():
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    solution = Solution()
    result = solution.longestOnes(nums, k)
    assert result == 6

def test_ex2():
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    solution = Solution()
    result = solution.longestOnes(nums, k)
    assert result == 10

def test_ex3():
    nums = [1,1,1,1,0,1,1,1]
    k = 0
    solution = Solution()
    result = solution.longestOnes(nums, k)
    assert result == 4

def test_ex4():
    nums = []
    k = 5
    solution = Solution()
    result = solution.longestOnes(nums, k)
    assert result == 0
