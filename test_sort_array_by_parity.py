from sort_array_by_parity import Solution


def test_ex1():
    nums = [3, 1, 2, 4]
    solution = Solution()
    result = solution.sortArrayByParity(nums)
    assert result == [2, 4, 1, 3]


def test_ex2():
    nums = [0]
    solution = Solution()
    result = solution.sortArrayByParity(nums)
    assert result == [0]
