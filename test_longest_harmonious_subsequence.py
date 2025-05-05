from longest_harmonious_subsequence import Solution

def test_ex1():
    nums = [1,3,2,2,5,2,3,7]
    solution = Solution()
    result = solution.findLHS(nums)
    assert result == 5

def test_ex2():
    nums = [1,2,3,4]
    solution = Solution()
    result = solution.findLHS(nums)
    assert result == 2

def test_ex3():
    nums = [1,1,1,1]
    solution = Solution()
    result = solution.findLHS(nums) 
    assert result == 0
