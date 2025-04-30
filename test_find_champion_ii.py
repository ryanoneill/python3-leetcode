from find_champion_ii import Solution

def test_ex1():
    n = 3
    edges = [[0,1],[1,2]]
    solution = Solution()
    result = solution.findChampion(n, edges)
    assert result == 0

def test_ex2():
    n = 4
    edges = [[0,2],[1,3],[1,2]]
    solution = Solution()
    result = solution.findChampion(n, edges)
    assert result == -1
