from house_robber_iii import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    data = "[3,2,3,null,3,null,1]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.rob(root)
    assert result == 7


def test_ex2():
    data = "[3,4,5,1,3,null,1]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.rob(root)
    assert result == 9
