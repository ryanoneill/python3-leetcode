from count_number_of_nice_subarrays import Solution

def test_ex1():
    nums = [1,1,2,1,1]
    k = 3
    solution = Solution()
    result = solution.numberOfSubarrays(nums, k)
    assert result == 2

def test_ex2():
    nums = [2,4,6]
    k = 1
    solution = Solution()
    result = solution.numberOfSubarrays(nums, k)
    assert result == 0

def test_ex3():
    nums = [2,2,2,1,2,2,1,2,2,2]
    k = 2
    solution = Solution()
    result = solution.numberOfSubarrays(nums, k)
    assert result == 16

