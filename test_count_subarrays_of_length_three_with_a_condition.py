from count_subarrays_of_length_three_with_a_condition import Solution

def test_ex1():
    nums = [1,2,1,4,1]
    solution = Solution()
    result = solution.countSubarrays(nums)
    assert result == 1

def test_ex2():
    nums = [1,1,1]
    solution = Solution()
    result = solution.countSubarrays(nums)
    assert result == 0
