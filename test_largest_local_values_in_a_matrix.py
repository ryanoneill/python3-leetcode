from largest_local_values_in_a_matrix import Solution

def test_ex1():
    grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    solution = Solution()
    result = solution.largestLocal(grid)
    assert result == [[9,9],[8,6]]

def test_ex2():
    grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    solution = Solution()
    result = solution.largestLocal(grid)
    assert result == [[2,2,2],[2,2,2],[2,2,2]]
