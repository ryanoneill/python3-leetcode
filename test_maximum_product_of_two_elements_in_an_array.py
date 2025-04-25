from maximum_product_of_two_elements_in_an_array import Solution


def test_ex1():
    nums = [3, 4, 5, 2]
    solution = Solution()
    result = solution.maxProduct(nums)
    assert result == 12


def test_ex2():
    nums = [1, 5, 4, 5]
    solution = Solution()
    result = solution.maxProduct(nums)
    assert result == 16


def test_ex3():
    nums = [3, 7]
    solution = Solution()
    result = solution.maxProduct(nums)
    assert result == 12
