from ransom_note import Solution


def test_ex1():
    ransomNote = "a"
    magazine = "b"
    solution = Solution()
    result = solution.canConstruct(ransomNote, magazine)
    assert not result


def test_ex2():
    ransomNote = "aa"
    magazine = "ab"
    solution = Solution()
    result = solution.canConstruct(ransomNote, magazine)
    assert not result


def test_ex3():
    ransomNote = "aa"
    magazine = "aab"
    solution = Solution()
    result = solution.canConstruct(ransomNote, magazine)
    assert result
