from find_subsequence_of_length_k_with_the_largest_sum import Solution

def test_ex1():
    nums = [2,1,3,3]
    k = 2
    solution = Solution()
    result = solution.maxSubsequence(nums, k)
    assert result == [3,3]

def test_ex2():
    nums = [-1,-2,3,4]
    k = 3
    solution = Solution()
    result = solution.maxSubsequence(nums, k)
    assert result == [-1,3,4]

def test_ex3():
    nums = [3,4,3,3]
    k = 2
    solution = Solution()
    result = solution.maxSubsequence(nums, k)
    assert result == [3,4]

