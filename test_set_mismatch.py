from set_mismatch import Solution

def test_ex1():
    nums = [1,2,2,4]
    solution = Solution()
    result = solution.findErrorNums(nums)
    assert result == [2,3]

def test_ex2():
    nums = [1,1]
    solution = Solution()
    result = solution.findErrorNums(nums)
    assert result == [1,2]
