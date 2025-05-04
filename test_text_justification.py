from text_justification import Solution


def test_ex1():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    solution = Solution()
    result = solution.fullJustify(words, maxWidth)
    assert result == ["This    is    an", "example  of text", "justification.  "]


def test_ex2():
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    solution = Solution()
    result = solution.fullJustify(words, maxWidth)
    assert result == ["What   must   be", "acknowledgment  ", "shall be        "]


def test_ex3():
    words = [
        "Science",
        "is",
        "what",
        "we",
        "understand",
        "well",
        "enough",
        "to",
        "explain",
        "to",
        "a",
        "computer.",
        "Art",
        "is",
        "everything",
        "else",
        "we",
        "do",
    ]
    maxWidth = 20
    solution = Solution()
    result = solution.fullJustify(words, maxWidth)
    assert result == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
