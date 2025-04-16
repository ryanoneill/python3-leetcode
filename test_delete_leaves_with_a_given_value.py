from delete_leaves_with_a_given_value import Solution
from serialize_and_deserialize_binary_tree import Codec

def test_ex1():
    data = "[1,2,3,2,null,2,4]"
    target = 2
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    remain = solution.removeLeafNodes(root, target)
    result = codec.serialize(remain)
    assert result == "[1,null,3,null,4]"

def test_ex2():
    data = "[1,3,3,3,2]"
    target = 3
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    remain = solution.removeLeafNodes(root, target)
    result = codec.serialize(remain)
    assert result == "[1,3,null,null,2]"

def test_ex3():
    data = "[1,2,null,2,null,2]" 
    target = 2
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    remain = solution.removeLeafNodes(root, target)
    result = codec.serialize(remain)
    assert result == "[1]"
