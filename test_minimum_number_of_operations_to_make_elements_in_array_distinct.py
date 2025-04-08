from minimum_number_of_operations_to_make_elements_in_array_distinct import Solution

def test_ex1():
    nums = [1,2,3,4,2,3,3,5,7]
    solution = Solution()
    result = solution.minimumOperations(nums)
    assert result == 2

def test_ex2():
    nums = [4,5,6,4,4]
    solution = Solution()
    result = solution.minimumOperations(nums)
    assert result == 2

def test_ex3():
    nums = [6,7,8,9]
    solution = Solution()
    result = solution.minimumOperations(nums)
    assert result == 0

def test_ex4():
    nums = [5,7,11,12,12]
    solution = Solution()
    result = solution.minimumOperations(nums)
    assert result == 2
