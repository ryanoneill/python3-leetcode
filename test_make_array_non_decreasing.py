from make_array_non_decreasing import Solution

def test_ex1():
    nums = [4,2,5,3,5]
    solution = Solution()
    result = solution.maximumPossibleSize(nums)
    assert result == 3

def test_ex2():
    nums = [1,2,3]
    solution = Solution()
    result = solution.maximumPossibleSize(nums)
    assert result == 3
