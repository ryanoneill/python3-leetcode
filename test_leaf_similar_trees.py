from leaf_similar_trees import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    data1 = "[3,5,1,6,2,9,8,null,null,7,4]"
    data2 = "[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]"
    codec = Codec()
    root1 = codec.deserialize(data1)
    root2 = codec.deserialize(data2)
    solution = Solution()
    result = solution.leafSimilar(root1, root2)
    assert result


def test_ex2():
    data1 = "[1,2,3]"
    data2 = "[1,3,2]"
    codec = Codec()
    root1 = codec.deserialize(data1)
    root2 = codec.deserialize(data2)
    solution = Solution()
    result = solution.leafSimilar(root1, root2)
    assert not result
