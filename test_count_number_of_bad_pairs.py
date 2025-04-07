from count_number_of_bad_pairs import Solution


def test_ex1():
    nums = [4, 1, 3, 3]
    solution = Solution()
    result = solution.countBadPairs(nums)
    assert result == 5


def test_ex2():
    nums = [1, 2, 3, 4, 5]
    solution = Solution()
    result = solution.countBadPairs(nums)
    assert result == 0
