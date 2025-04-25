from serialize_and_deserialize_n_ary_tree import Codec
from n_ary_tree_postorder_traversal import Solution


def test_ex1():
    data = "[1,null,3,2,4,null,5,6]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.postorder(root)
    assert result == [5, 6, 3, 2, 4, 1]


def test_ex2():
    data = "[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.postorder(root)
    assert result == [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
