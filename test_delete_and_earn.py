from delete_and_earn import Solution

def test_ex1():
    nums = [3,4,2]
    solution = Solution()
    result = solution.deleteAndEarn(nums)
    assert result == 6

def test_ex2():
    nums = [2,2,3,3,3,4]
    solution = Solution()
    result = solution.deleteAndEarn(nums)
    assert result == 9
