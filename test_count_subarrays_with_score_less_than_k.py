from count_subarrays_with_score_less_than_k import Solution

def test_ex1():
    nums = [2,1,4,3,5]
    k = 10
    solution = Solution()
    result = solution.countSubarrays(nums, k)
    assert result == 6

def test_ex2():
    nums = [1,1,1]
    k = 5
    solution = Solution()
    result = solution.countSubarrays(nums, k)
    assert result == 5
