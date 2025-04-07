from counting_elements import Solution


def test_ex1():
    arr = [1, 2, 3]
    solution = Solution()
    result = solution.countElements(arr)
    assert result == 2


def test_ex2():
    arr = [1, 1, 3, 3, 5, 5, 7, 7]
    solution = Solution()
    result = solution.countElements(arr)
    assert result == 0
