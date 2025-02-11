from remove_all_occurrences_of_a_substring import Solution

def test_ex1():
    s = "daabcbaabcbc"
    part = "abc"
    solution = Solution()
    result = solution.removeOccurrences(s, part)
    assert result == "dab"

# def test_ex2():
#     s = "axxxxyyyyb"
#     part = "xy"
#     solution = Solution()
#     result = solution.removeOccurrences(s, part)
#     assert result == "ab"
