from divide_array_into_equal_pairs import Solution


def test_ex1():
    nums = [3, 2, 3, 2, 2, 2]
    solution = Solution()
    result = solution.divideArray(nums)
    assert result


def test_ex2():
    nums = [1, 2, 3, 4]
    solution = Solution()
    result = solution.divideArray(nums)
    assert not result
