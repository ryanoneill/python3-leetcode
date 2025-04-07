from construct_the_lexicographically_largest_valid_sequence import Solution


def test_ex1():
    n = 3
    solution = Solution()
    result = solution.constructDistancedSequence(n)
    assert result == [3, 1, 2, 3, 2]


def test_ex2():
    n = 5
    solution = Solution()
    result = solution.constructDistancedSequence(n)
    assert result == [5, 3, 1, 4, 3, 5, 2, 4, 2]


def test_ex3():
    n = 1
    solution = Solution()
    result = solution.constructDistancedSequence(n)
    assert result == [1]


def test_ex4():
    n = 4
    solution = Solution()
    result = solution.constructDistancedSequence(n)
    assert result == [4, 2, 3, 2, 4, 3, 1]


def test_ex5():
    n = 2
    solution = Solution()
    result = solution.constructDistancedSequence(n)
    assert result == [2, 1, 2]
