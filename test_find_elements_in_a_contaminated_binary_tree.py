from find_elements_in_a_contaminated_binary_tree import FindElements
from serialize_and_deserialize_binary_tree import Codec

def test_ex1():
    items = "[-1,null,-1]"
    codec = Codec()
    root = codec.deserialize(items)
    fe = FindElements(root)
    assert not fe.find(1)
    assert fe.find(2)

def test_ex2():
    items = "[-1,-1,-1,-1,-1]"
    codec = Codec()
    root = codec.deserialize(items)
    fe = FindElements(root)
    assert fe.find(1)
    assert fe.find(3)
    assert not fe.find(5)

