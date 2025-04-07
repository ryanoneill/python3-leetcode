from serialize_and_deserialize_binary_tree import Codec
from insert_into_binary_search_tree import Solution


def test_ex1():
    root = "[4,2,7,1,3]"
    val = 5
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.insertIntoBST(head, val)
    assert codec.serialize(result) == "[4,2,7,1,3,5]"


def test_ex2():
    root = "[40,20,60,10,30,50,70]"
    val = 25
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.insertIntoBST(head, val)
    assert codec.serialize(result) == "[40,20,60,10,30,50,70,null,null,25]"


def test_ex3():
    root = "[4,2,7,1,3,null,null,null,null,null,null]"
    val = 5
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.insertIntoBST(head, val)
    assert codec.serialize(result) == "[4,2,7,1,3,5]"
