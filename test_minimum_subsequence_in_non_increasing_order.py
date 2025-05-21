from minimum_subsequence_in_non_increasing_order import Solution

def test_ex1():
    nums = [4,3,10,9,8]
    solution = Solution()
    result = solution.minSubsequence(nums)
    assert result == [10,9]

def test_ex2():
    nums = [4,4,7,6,7]
    solution = Solution()
    result = solution.minSubsequence(nums)
    assert result == [7,7,6]
