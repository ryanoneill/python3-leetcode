from find_players_with_zero_or_one_losses import Solution


def test_ex1():
    matches = [
        [1, 3],
        [2, 3],
        [3, 6],
        [5, 6],
        [5, 7],
        [4, 5],
        [4, 8],
        [4, 9],
        [10, 4],
        [10, 9],
    ]
    solution = Solution()
    result = solution.findWinners(matches)
    assert result == [[1, 2, 10], [4, 5, 7, 8]]


def test_ex2():
    matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
    solution = Solution()
    result = solution.findWinners(matches)
    assert result == [[1, 2, 5, 6], []]
