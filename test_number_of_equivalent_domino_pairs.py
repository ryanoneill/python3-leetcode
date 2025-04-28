from number_of_equivalent_domino_pairs import Solution

def test_ex1():
    dominoes = [[1,2],[2,1],[3,4],[5,6]]
    solution = Solution()
    result = solution.numEquivDominoPairs(dominoes)
    assert result == 1 

def test_ex2():
    dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    solution = Solution()
    result = solution.numEquivDominoPairs(dominoes)
    assert result == 3

