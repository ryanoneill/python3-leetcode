from find_if_path_exists_in_graph import Solution

def test_ex1():
    solution = Solution()
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    result = solution.validPath(n, edges, source, destination)
    assert result

def test_ex2():
    solution = Solution()
    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5
    result = solution.validPath(n, edges, source, destination)
    assert not result

def test_ex3():
    solution = Solution()
    n = 1
    edges = []
    source = 0
    destination = 0
    result = solution.validPath(n, edges, source, destination)
    assert result

