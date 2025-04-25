from count_of_interesting_subarrays import Solution

def test_ex1():
    nums = [3,2,4]
    modulo = 2
    k = 1
    solution = Solution()
    result = solution.countInterestingSubarrays(nums, modulo, k)
    assert result == 3

def test_ex2():
    nums = [3,1,9,6]
    modulo = 3
    k = 0
    solution = Solution()
    result = solution.countInterestingSubarrays(nums, modulo, k)
    assert result == 2
