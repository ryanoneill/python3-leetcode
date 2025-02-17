from letter_tile_possibilities import Solution

def test_ex1():
    tiles = "AAB"
    solution = Solution()
    result = solution.numTilePossibilities(tiles)
    assert result == 8

def test_ex2():
    tiles = "AAABBC"
    solution = Solution()
    result = solution.numTilePossibilities(tiles)
    assert result == 188

def test_ex3():
    tiles = "V"
    solution = Solution()
    result = solution.numTilePossibilities(tiles)
    assert result == 1
