from remove_colored_pieces_if_both_neighbors_are_the_same_color import Solution

def test_ex1():
    colors = "AAABABB"
    solution = Solution()
    result = solution.winnerOfGame(colors)
    assert result

def test_ex2():
    colors = "AA"
    solution = Solution()
    result = solution.winnerOfGame(colors)
    assert not result

def test_ex3():
    colors = "ABBBBBBBAAA"
    solution = Solution()
    result = solution.winnerOfGame(colors)
    assert not result
