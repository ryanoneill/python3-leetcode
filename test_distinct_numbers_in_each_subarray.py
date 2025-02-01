from distinct_numbers_in_each_subarray import Solution

def test_ex1():
    nums = [1,2,3,2,2,1,3]
    k = 3
    solution = Solution()
    result = solution.distinctNumbers(nums, k)
    assert result == [3,2,2,2,3]

def test_ex2():
    nums = [1,1,1,1,2,3,4]
    k = 4
    solution = Solution()
    result = solution.distinctNumbers(nums, k)
    assert result == [1,2,3,4]
