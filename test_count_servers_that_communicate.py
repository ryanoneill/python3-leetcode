from count_servers_that_communicate import Solution

def test_ex1():
    grid = [[1,0],[0,1]]
    solution = Solution()
    result = solution.countServers(grid)
    assert result == 0

def test_ex2():
    grid = [[1,0],[1,1]]
    solution = Solution()
    result = solution.countServers(grid)
    assert result == 3

def test_ex3():
    grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    solution = Solution()
    result = solution.countServers(grid)
    assert result == 4
