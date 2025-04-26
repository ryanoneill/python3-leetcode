from binary_subarrays_with_sum import Solution

def test_ex1():
    nums = [1,0,1,0,1]
    goal = 2
    solution = Solution()
    result = solution.numSubarraysWithSum(nums, goal)
    assert result == 4

def test_ex2():
    nums = [0,0,0,0,0]
    goal = 0
    solution = Solution()
    result = solution.numSubarraysWithSum(nums, goal)
    assert result == 15

def test_ex3():
    nums = [0,0,0,0,0,0,1,0,0,0]
    goal = 0
    solution = Solution()
    result = solution.numSubarraysWithSum(nums, goal)
    assert result == 27
