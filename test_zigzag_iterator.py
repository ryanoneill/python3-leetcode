from zigzag_iterator import ZigzagIterator


def test_ex1():
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    zi = ZigzagIterator(v1, v2)
    results = []
    while zi.hasNext():
        results.append(zi.next())
    assert results == [1, 3, 2, 4, 5, 6]


def test_ex2():
    v1 = [1]
    v2 = []
    zi = ZigzagIterator(v1, v2)
    results = []
    while zi.hasNext():
        results.append(zi.next())
    assert results == [1]


def test_ex3():
    v1 = []
    v2 = [1]
    zi = ZigzagIterator(v1, v2)
    results = []
    while zi.hasNext():
        results.append(zi.next())
    assert results == [1]
