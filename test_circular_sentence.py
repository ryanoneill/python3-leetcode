from circular_sentence import Solution


def test_ex1():
    sentence = "leetcode exercises sound delightful"
    solution = Solution()
    result = solution.isCircularSentence(sentence)
    assert result


def test_ex2():
    sentence = "eetcode"
    solution = Solution()
    result = solution.isCircularSentence(sentence)
    assert result


def test_ex3():
    sentence = "Leetcode is cool"
    solution = Solution()
    result = solution.isCircularSentence(sentence)
    assert not result
