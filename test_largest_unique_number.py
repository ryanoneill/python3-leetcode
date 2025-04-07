from largest_unique_number import Solution


def test_ex1():
    nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    solution = Solution()
    result = solution.largestUniqueNumber(nums)
    assert result == 8


def test_ex2():
    nums = [9, 9, 8, 8]
    solution = Solution()
    result = solution.largestUniqueNumber(nums)
    assert result == -1
