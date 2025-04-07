from alternating_groups_i import Solution


def test_ex1():
    colors = [1, 1, 1]
    solution = Solution()
    result = solution.numberOfAlternatingGroups(colors)
    assert result == 0


def test_ex2():
    colors = [0, 1, 0, 0, 1]
    solution = Solution()
    result = solution.numberOfAlternatingGroups(colors)
    assert result == 3
