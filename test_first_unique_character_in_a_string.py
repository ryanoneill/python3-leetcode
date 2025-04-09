from first_unique_character_in_a_string import Solution

def test_ex1():
    s = "leetcode"
    solution = Solution()
    result = solution.firstUniqChar(s)
    assert result == 0

def test_ex2():
    s = "loveleetcode"
    solution = Solution()
    result = solution.firstUniqChar(s)
    assert result == 2

def test_ex3():
    s = "aabb"
    solution = Solution()
    result = solution.firstUniqChar(s)
    assert result == -1
