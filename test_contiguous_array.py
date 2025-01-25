from contiguous_array import Solution

def test_ex1():
    nums = [0,1]
    solution = Solution()
    result = solution.findMaxLength(nums)
    assert result == 2

def test_ex2():
    nums = [0,1,0]
    solution = Solution()
    result = solution.findMaxLength(nums)
    assert result == 2
