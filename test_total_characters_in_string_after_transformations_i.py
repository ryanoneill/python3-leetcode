from total_characters_in_string_after_transformations_i import Solution

def test_ex1():
    s = "abcyy"
    t = 2
    solution = Solution()
    result = solution.lengthAfterTransformations(s, t)
    assert result == 7

def test_ex2():
    s = "azbk"
    t = 1
    solution = Solution()
    result = solution.lengthAfterTransformations(s, t)
    assert result == 5

def test_ex3():
    s = "jqktcurgdvlibczdsvnsg"
    t = 7517
    solution = Solution()
    result = solution.lengthAfterTransformations(s, t)
    assert result == 79033769
