from remove_duplicate_letters import Solution

def test_ex1():
    s = "bcabc"
    solution = Solution()
    result = solution.removeDuplicateLetters(s)
    assert result == "abc"

def test_ex2():
    s = "cbacdcbc"
    solution = Solution()
    result = solution.removeDuplicateLetters(s)
    assert result == "acdb"
