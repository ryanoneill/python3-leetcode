from reorganize_string import Solution

def test_ex1():
    s = "aab"
    solution = Solution()
    result = solution.reorganizeString(s)
    assert result == "aba"

# def test_ex2():
#     s = "aaab"
#     solution = Solution()
#     result = solution.reorganizeString(s)
#     assert result == ""
