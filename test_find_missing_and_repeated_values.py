from find_missing_and_repeated_values import Solution

def test_ex1():
    grid = [[1,3],[2,2]]
    solution = Solution()
    result = solution.findMissingAndRepeatedValues(grid)
    assert result == [2, 4]

def test_ex2():
    grid = [[9,1,7],[8,9,2],[3,4,6]]
    solution = Solution()
    result = solution.findMissingAndRepeatedValues(grid)
    assert result == [9, 5]
