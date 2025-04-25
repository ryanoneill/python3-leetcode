from second_minimum_node_in_a_binary_tree import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    data = "[2,2,5,null,null,5,7]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.findSecondMinimumValue(root)
    assert result == 5


def test_ex2():
    data = "[2,2,2]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.findSecondMinimumValue(root)
    assert result == -1


def test_ex3():
    data = "[1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.findSecondMinimumValue(root)
    assert result == 2
