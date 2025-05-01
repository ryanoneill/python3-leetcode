from next_greater_element_ii import Solution

def test_ex1():
    nums = [1,2,1]
    solution = Solution()
    result = solution.nextGreaterElements(nums)
    assert result == [2,-1,2]

def test_ex2():
    nums = [1,2,3,4,3]
    solution = Solution()
    result = solution.nextGreaterElements(nums)
    assert result == [2,3,4,-1,4]
