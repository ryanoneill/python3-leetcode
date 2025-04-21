from count_the_hidden_sequences import Solution

def test_ex1():
    differences = [1, -3, 4]
    lower = 1
    upper = 6
    solution = Solution()
    result = solution.numberOfArrays(differences, lower, upper)
    assert result == 2

def test_ex2():
    differences = [3, -4, 5, 1, -2]
    lower = -4
    upper = 5
    solution = Solution()
    result = solution.numberOfArrays(differences, lower, upper)
    assert result == 4

def test_ex3():
    differences = [4, -7, 2]
    lower = 3
    upper = 6
    solution = Solution()
    result = solution.numberOfArrays(differences, lower, upper)
    assert result == 0
