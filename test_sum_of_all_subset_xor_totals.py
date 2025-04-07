from sum_of_all_subset_xor_totals import Solution


def test_ex1():
    nums = [1, 3]
    solution = Solution()
    result = solution.subsetXORSum(nums)
    assert result == 6


def test_ex2():
    nums = [5, 1, 6]
    solution = Solution()
    result = solution.subsetXORSum(nums)
    assert result == 28
