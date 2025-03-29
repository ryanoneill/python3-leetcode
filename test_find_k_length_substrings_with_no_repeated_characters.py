from find_k_length_substrings_with_no_repeated_characters import Solution

def test_ex1():
    s = "havefunonleetcode"
    k = 5
    solution = Solution()
    result = solution.numKLenSubstrNoRepeats(s, k)
    assert result == 6

def test_ex2():
    s = "home"
    k = 5
    solution = Solution()
    result = solution.numKLenSubstrNoRepeats(s, k)
    assert result == 0
