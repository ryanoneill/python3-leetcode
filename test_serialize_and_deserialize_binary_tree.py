from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    root = "[1,2,3,null,null,4,5]"
    codec = Codec()
    result = codec.deserialize(root)
    result = codec.serialize(result)
    assert result == root


def test_ex2():
    root = "[]"
    codec = Codec()
    result = codec.deserialize(root)
    result = codec.serialize(result)
    assert result == root


def test_ex3():
    root = "[1,2,3,4,5,6,7,8]"
    codec = Codec()
    result = codec.deserialize(root)
    result = codec.serialize(result)
    assert result == root


def test_ex4():
    root = "[2,null,3,null,4,null,5,null,6]"
    codec = Codec()
    result = codec.deserialize(root)
    result = codec.serialize(result)
    assert result == root


def test_ex5():
    root = "[5,4,8,11,null,13,4,7,2,null,null,null,1]"
    codec = Codec()
    result = codec.deserialize(root)
    result = codec.serialize(result)
    assert result == root


def test_ex6():
    root = "[1,2]"
    codec = Codec()
    result = codec.deserialize(root)
    result = codec.serialize(result)
    assert result == root


def test_ex7():
    root = "[1,-2,-3,1,3,-2,null,-1]"
    codec = Codec()
    result = codec.deserialize(root)
    result = codec.serialize(result)
    assert result == root
