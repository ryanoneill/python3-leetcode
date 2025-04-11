from path_crossing import Solution

def test_ex1():
    path = "NES"
    solution = Solution()
    result = solution.isPathCrossing(path)
    assert not result

def test_ex2():
    path = "NESWW"
    solution = Solution()
    result = solution.isPathCrossing(path)
    assert result

def test_ex3():
    path = "WSSESEEE"
    solution = Solution()
    result = solution.isPathCrossing(path)
    assert not result
