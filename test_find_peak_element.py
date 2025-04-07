from find_peak_element import Solution


def test_ex1():
    nums = [1, 2, 3, 1]
    solution = Solution()
    result = solution.findPeakElement(nums)
    assert result == 2


def test_ex2():
    nums = [1, 2, 1, 3, 5, 6, 4]
    solution = Solution()
    result = solution.findPeakElement(nums)
    assert result == 5
