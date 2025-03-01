from apply_operations_to_an_array import Solution

def test_ex1():
    nums = [1,2,2,1,1,0]
    solution = Solution()
    result = solution.applyOperations(nums)
    assert result == [1,4,2,0,0,0]

def test_ex2():
    nums = [0,1]
    solution = Solution()
    result = solution.applyOperations(nums)
    assert result == [1,0]
