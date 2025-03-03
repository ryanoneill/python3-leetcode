from partition_array_according_to_given_pivot import Solution

def test_ex1():
    nums = [9,12,5,10,14,3,10]
    pivot = 10
    solution = Solution()
    result = solution.pivotArray(nums, pivot)
    assert result == [9,5,3,10,10,12,14]

def test_ex2():
    nums = [-3,4,3,2]
    pivot = 2
    solution = Solution()
    result = solution.pivotArray(nums, pivot)
    assert result == [-3,2,4,3]
