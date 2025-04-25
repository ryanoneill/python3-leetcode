from rabbits_in_forest import Solution


def test_ex1():
    answers = [1, 1, 2]
    solution = Solution()
    result = solution.numRabbits(answers)
    assert result == 5


def test_ex2():
    answers = [10, 10, 10]
    solution = Solution()
    result = solution.numRabbits(answers)
    assert result == 11
