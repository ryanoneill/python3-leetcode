from rearrange_spaces_between_words import Solution

def test_ex1():
    text = "  this   is  a sentence "
    solution = Solution()
    result = solution.reorderSpaces(text)
    assert result == "this   is   a   sentence"

def test_ex2():
    text = " practice   makes   perfect"
    solution = Solution()
    result = solution.reorderSpaces(text)
    assert result == "practice   makes   perfect "

def test_ex3():
    text = "a"
    solution = Solution()
    result = solution.reorderSpaces(text)
    assert result == "a"

def test_ex4():
    text = "   abc     123 "
    solution = Solution()
    result = solution.reorderSpaces(text)
    assert result == "abc         123"

def test_ex5():
    text = "a b   c d"
    solution = Solution()
    result = solution.reorderSpaces(text)
    assert result == "a b c d  "
