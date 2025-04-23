from degree_of_an_array import Solution

def test_ex1():
    nums = [1,2,2,3,1]
    solution = Solution()
    result = solution.findShortestSubArray(nums)
    assert result == 2

def test_ex2():
    nums = [1,2,2,3,1,4,2]
    solution = Solution()
    result = solution.findShortestSubArray(nums)
    assert result == 6
