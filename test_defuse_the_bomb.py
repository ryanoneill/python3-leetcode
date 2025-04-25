from defuse_the_bomb import Solution


def test_ex1():
    code = [5, 7, 1, 4]
    k = 3
    solution = Solution()
    result = solution.decrypt(code, k)
    assert result == [12, 10, 16, 13]


def test_ex2():
    code = [1, 2, 3, 4]
    k = 0
    solution = Solution()
    result = solution.decrypt(code, k)
    assert result == [0, 0, 0, 0]


def test_ex3():
    code = [2, 4, 9, 3]
    k = -2
    solution = Solution()
    result = solution.decrypt(code, k)
    assert result == [12, 5, 6, 13]
