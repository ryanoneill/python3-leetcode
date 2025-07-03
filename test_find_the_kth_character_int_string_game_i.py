from find_the_kth_character_in_string_game_i import Solution

def test_ex1():
    solution = Solution()
    k = 5
    result = solution.kthCharacter(k)
    assert result == "b"

def test_ex2():
    solution = Solution()
    k = 10
    result = solution.kthCharacter(k)
    assert result == "c"
