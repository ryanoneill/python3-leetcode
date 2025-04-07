from minimum_swaps_to_group_all_1s_together import Solution


def test_ex1():
    data = [1, 0, 1, 0, 1]
    solution = Solution()
    result = solution.minSwaps(data)
    assert result == 1


def test_ex2():
    data = [0, 0, 0, 1, 0]
    solution = Solution()
    result = solution.minSwaps(data)
    assert result == 0


def test_ex3():
    data = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]
    solution = Solution()
    result = solution.minSwaps(data)
    assert result == 3
