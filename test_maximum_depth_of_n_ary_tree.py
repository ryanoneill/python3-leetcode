from maximum_depth_of_n_ary_tree import Solution
from serialize_and_deserialize_n_ary_tree import Codec

def test_ex1():
    data = "[1,null,3,2,4,null,5,6]"
    codec = Codec()
    items = codec.deserialize(data)
    solution = Solution()
    result = solution.maxDepth(items)
    assert result == 3

def test_ex2():
    data = "[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]"
    codec = Codec()
    items = codec.deserialize(data)
    solution = Solution()
    result = solution.maxDepth(items)
    assert result == 5

def test_ex3():
    data = "[]"
    codec = Codec()
    items = codec.deserialize(data)
    solution = Solution()
    result = solution.maxDepth(items)
    assert result == 0
