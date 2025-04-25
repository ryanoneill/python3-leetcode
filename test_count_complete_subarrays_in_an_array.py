from count_complete_subarrays_in_an_array import Solution


def test_ex1():
    nums = [1, 3, 1, 2, 2]
    solution = Solution()
    result = solution.countCompleteSubarrays(nums)
    assert result == 4


def test_ex2():
    nums = [5, 5, 5, 5]
    solution = Solution()
    result = solution.countCompleteSubarrays(nums)
    assert result == 10
