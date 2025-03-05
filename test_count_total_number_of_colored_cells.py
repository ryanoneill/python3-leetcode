from count_total_number_of_colored_cells import Solution

def test_ex1():
    n = 1
    solution = Solution()
    result = solution.coloredCells(n)
    assert result == 1

def test_ex2():
    n = 2
    solution = Solution()
    result = solution.coloredCells(n)
    assert result == 5

def test_ex3():
    n = 3
    solution = Solution()
    result = solution.coloredCells(n)
    assert result == 13

def test_ex4():
    n = 4
    solution = Solution()
    result = solution.coloredCells(n)
    assert result == 25

def test_ex5():
    n = 5
    solution = Solution()
    result = solution.coloredCells(n)
    assert result == 41
