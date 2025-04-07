from tuple_with_same_product import Solution


def test_ex1():
    nums = [2, 3, 4, 6]
    solution = Solution()
    result = solution.tupleSameProduct(nums)
    assert result == 8


def test_ex2():
    nums = [1, 2, 4, 5, 10]
    solution = Solution()
    result = solution.tupleSameProduct(nums)
    assert result == 16


def test_ex3():
    nums = [2, 3, 4, 6, 8, 12]
    solution = Solution()
    result = solution.tupleSameProduct(nums)
    assert result == 40
