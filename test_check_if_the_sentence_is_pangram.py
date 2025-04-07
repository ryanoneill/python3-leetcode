from check_if_the_sentence_is_pangram import Solution


def test_ex1():
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    solution = Solution()
    result = solution.checkIfPangram(sentence)
    assert result


def test_ex2():
    sentence = "leetcode"
    solution = Solution()
    result = solution.checkIfPangram(sentence)
    assert not result
