from alternating_groups_ii import Solution


def test_ex1():
    colors = [0, 1, 0, 1, 0]
    k = 3
    solution = Solution()
    result = solution.numberOfAlternatingGroups(colors, k)
    assert result == 3


def test_ex2():
    colors = [0, 1, 0, 0, 1, 0, 1]
    k = 6
    solution = Solution()
    result = solution.numberOfAlternatingGroups(colors, k)
    assert result == 2


def test_ex3():
    colors = [1, 1, 0, 1]
    k = 4
    solution = Solution()
    result = solution.numberOfAlternatingGroups(colors, k)
    assert result == 0
