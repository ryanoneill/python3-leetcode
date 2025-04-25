from uncommon_words_from_two_sentences import Solution


def test_ex1():
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    solution = Solution()
    result = solution.uncommonFromSentences(s1, s2)
    assert result == ["sweet", "sour"]


def test_ex2():
    s1 = "apple apple"
    s2 = "banana"
    solution = Solution()
    result = solution.uncommonFromSentences(s1, s2)
    assert result == ["banana"]
