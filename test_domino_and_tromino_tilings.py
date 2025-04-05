from domino_and_tromino_tilings import Solution

def test_ex1():
    n = 3
    solution = Solution()
    result = solution.numTilings(n)
    assert result == 5

def test_ex2():
    n = 1
    solution = Solution()
    result = solution.numTilings(n)
    assert result == 1

def test_ex3():
    n = 10
    solution = Solution()
    result = solution.numTilings(n)
    assert result == 1255
