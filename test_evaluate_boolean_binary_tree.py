from evaluate_boolean_binary_tree import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    data = "[2,1,3,null,null,0,1]"
    codec = Codec()
    items = codec.deserialize(data)
    solution = Solution()
    result = solution.evaluateTree(items)
    assert result


def test_ex2():
    data = "[0]"
    codec = Codec()
    items = codec.deserialize(data)
    solution = Solution()
    result = solution.evaluateTree(items)
    assert not result
