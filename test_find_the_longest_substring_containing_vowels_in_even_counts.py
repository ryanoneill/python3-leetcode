from find_the_longest_substring_containing_vowels_in_even_counts import Solution

def test_ex1():
    s = "eleetminicoworoep"
    solution = Solution()
    result = solution.findTheLongestSubstring(s)
    assert result == 13

def test_ex2():
    s = "leetcodeisgreat"
    solution = Solution()
    result = solution.findTheLongestSubstring(s)
    assert result == 5

def test_ex3():
    s = "bcbcbc"
    solution = Solution()
    result = solution.findTheLongestSubstring(s)
    assert result == 6
