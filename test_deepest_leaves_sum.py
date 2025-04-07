from deepest_leaves_sum import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    root = "[1,2,3,4,5,null,6,7,null,null,null,null,8]"
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.deepestLeavesSum(head)
    assert result == 15


def test_ex2():
    root = "[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]"
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.deepestLeavesSum(head)
    assert result == 19
