from max_consecutive_ones_ii import Solution

def test_ex1():
    nums = [1,0,1,1,0]
    solution = Solution()
    result = solution.findMaxConsecutiveOnes(nums)
    assert result == 4

def test_ex2():
    nums = [1,0,1,1,0,1]
    solution = Solution()
    result = solution.findMaxConsecutiveOnes(nums)
    assert result == 4
