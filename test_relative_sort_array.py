from relative_sort_array import Solution


def test_ex1():
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    solution = Solution()
    result = solution.relativeSortArray(arr1, arr2)
    assert result == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]


def test_ex2():
    arr1 = [28, 6, 22, 8, 44, 17]
    arr2 = [22, 28, 8, 6]
    solution = Solution()
    result = solution.relativeSortArray(arr1, arr2)
    assert result == [22, 28, 8, 6, 17, 44]
