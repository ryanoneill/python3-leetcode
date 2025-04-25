from make_two_arrays_equal_by_reversing_subarrays import Solution


def test_ex1():
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    solution = Solution()
    result = solution.canBeEqual(target, arr)
    assert result


def test_ex2():
    target = [7]
    arr = [7]
    solution = Solution()
    result = solution.canBeEqual(target, arr)
    assert result


def test_ex3():
    target = [3, 7, 9]
    arr = [3, 7, 11]
    solution = Solution()
    result = solution.canBeEqual(target, arr)
    assert not result
