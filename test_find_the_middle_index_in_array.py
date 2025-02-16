from find_the_middle_index_in_array import Solution

def test_ex1():
    nums = [2,3,-1,8,4]
    solution = Solution()
    result = solution.findMiddleIndex(nums)
    assert result == 3

def test_ex2():
    nums = [1,-1,4]
    solution = Solution()
    result = solution.findMiddleIndex(nums)
    assert result == 2

def test_ex3():
    nums = [1,2,3,4]
    solution = Solution()
    result = solution.findMiddleIndex(nums)
    assert result == -1
