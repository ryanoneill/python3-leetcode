from missing_number import Solution

def test_ex1():
    nums = [3,0,1]
    solution = Solution()
    result = solution.missingNumber(nums)
    assert result == 2

def test_ex2():
    nums = [0,1]
    solution = Solution()
    result = solution.missingNumber(nums)
    assert result == 2

def test_ex3():
    nums = [9,6,4,2,3,5,7,0,1]
    solution = Solution()
    result = solution.missingNumber(nums)
    assert result == 8
