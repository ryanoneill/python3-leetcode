from append_characters_to_string_to_make_subsequence import Solution

def test_ex1():
    s = "coaching"
    t = "coding"
    solution = Solution()
    result = solution.appendCharacters(s, t)
    assert result == 4

def test_ex2():
    s = "abcde"
    t = "a"
    solution = Solution()
    result = solution.appendCharacters(s, t)
    assert result == 0

def test_ex3():
    s = "z"
    t = "abcde"
    solution = Solution()
    result = solution.appendCharacters(s, t)
    assert result == 5
