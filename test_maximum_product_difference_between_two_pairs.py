from maximum_product_difference_between_two_pairs import Solution


def test_ex1():
    nums = [5, 6, 2, 7, 4]
    solution = Solution()
    result = solution.maxProductDifference(nums)
    assert result == 34


def test_ex2():
    nums = [4, 2, 5, 9, 7, 4, 8]
    solution = Solution()
    result = solution.maxProductDifference(nums)
    assert result == 64
