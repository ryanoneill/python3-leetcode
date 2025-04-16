from find_the_town_judge import Solution

def test_ex1():
    n = 2
    trust = [[1,2]]
    solution = Solution()
    result = solution.findJudge(n, trust)
    assert result == 2

def test_ex2():
    n = 3
    trust = [[1,3],[2,3]]
    solution = Solution()
    result = solution.findJudge(n, trust)
    assert result == 3

def test_ex3():
    n = 3
    trust = [[1,3],[2,3],[3,1]]
    solution = Solution()
    result = solution.findJudge(n, trust)
    assert result == -1
