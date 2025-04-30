from find_all_anagrams_in_a_string import Solution

def test_ex1():
    s = "cbaebabacd"
    p = "abc"
    solution = Solution()
    result = solution.findAnagrams(s, p)
    assert result == [0,6]

def test_ex2():
    s = "abab"
    p = "ab"
    solution = Solution()
    result = solution.findAnagrams(s, p)
    assert result == [0,1,2]
