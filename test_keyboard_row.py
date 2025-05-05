from keyboard_row import Solution

def test_ex1():
    words = ["Hello", "Alaska", "Dad", "Peace"]
    solution = Solution()
    result = solution.findWords(words)
    assert result == ["Alaska", "Dad"]

def test_ex2():
    words = ["omk"]
    solution = Solution()
    result = solution.findWords(words)
    assert result == []

def test_ex3():
    words = ["adsdf", "sfd"]
    solution = Solution()
    result = solution.findWords(words)
    assert result == ["adsdf", "sfd"]
