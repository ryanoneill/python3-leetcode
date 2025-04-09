from minimum_operations_to_make_array_values_equal_to_k import Solution

def test_ex1():
    nums = [5,2,5,4,5]
    k = 2
    solution = Solution()
    result = solution.minOperations(nums, k)
    assert result == 2

def test_ex2():
    nums = [2,1,2]
    k = 2
    solution = Solution()
    result = solution.minOperations(nums, k)
    assert result == -1
