from jewels_and_stones import Solution


def test_ex1():
    jewels = "aA"
    stones = "aAAbbbb"
    solution = Solution()
    result = solution.numJewelsInStones(jewels, stones)
    assert result == 3


def test_ex2():
    jewels = "z"
    stones = "ZZ"
    solution = Solution()
    result = solution.numJewelsInStones(jewels, stones)
    assert result == 0
