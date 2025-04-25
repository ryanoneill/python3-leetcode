from count_equal_and_divisible_pairs_in_an_array import Solution


def test_ex1():
    nums = [3, 1, 2, 2, 2, 1, 3]
    k = 2
    solution = Solution()
    result = solution.countPairs(nums, k)
    assert result == 4


def test_ex2():
    nums = [1, 2, 3, 4]
    k = 1
    solution = Solution()
    result = solution.countPairs(nums, k)
    assert result == 0
