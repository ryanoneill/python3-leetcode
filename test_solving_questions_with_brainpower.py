from solving_questions_with_brainpower import Solution


def test_ex1():
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    solution = Solution()
    result = solution.mostPoints(questions)
    assert result == 5


def test_ex2():
    questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    solution = Solution()
    result = solution.mostPoints(questions)
    assert result == 7
