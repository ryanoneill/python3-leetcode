from verifying_an_alien_dictionary import Solution

def test_ex1():
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    solution = Solution()
    result = solution.isAlienSorted(words, order)
    assert result

def test_ex2():
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    solution = Solution()
    result = solution.isAlienSorted(words, order)
    assert not result

def test_ex3():
    words = ["apple","app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    solution = Solution()
    result = solution.isAlienSorted(words, order)
    assert not result

def test_ex4():
    words = ["zirqhpfscx","zrmvtxgelh","vokopzrtc","nugfyso","rzdmvyf","vhvqzkfqis","dvbkppw","ttfwryy","dodpbbkp","akycwwcdog"]
    order = "khjzlicrmunogwbpqdetasyfvx"
    solution = Solution()
    result = solution.isAlienSorted(words, order)
    assert not result
