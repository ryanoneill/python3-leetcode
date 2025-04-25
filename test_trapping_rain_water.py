from trapping_rain_water import Solution


def test_ex1():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solution = Solution()
    result = solution.trap(height)
    assert result == 6


def test_ex2():
    height = [4, 2, 0, 3, 2, 5]
    solution = Solution()
    result = solution.trap(height)
    assert result == 9
