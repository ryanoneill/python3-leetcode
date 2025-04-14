import random

from collections import deque
from find_root_of_n_ary_tree import Solution
from node import Node
from serialize_and_deserialize_n_ary_tree import Codec
from typing import Optional, List

def traverse(root: Optional[Node]) -> List[Node]:
    results = []
    queue = deque()
    queue.append(root)
    while queue:
        item = queue.popleft()
        results.append(item)
        for child in item.children:
            queue.append(child)

    random.shuffle(results)

    return results

def test_ex1():
    data = "[1,null,3,2,4,null,5,6]"
    codec = Codec()
    root = codec.deserialize(data)
    nodes = traverse(root)
    solution = Solution()
    result = solution.findRoot(nodes)
    serialized = codec.serialize(result)
    assert data == serialized

def test_ex2():
    data = "[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]"
    codec = Codec()
    root = codec.deserialize(data)
    nodes = traverse(root)
    solution = Solution()
    result = solution.findRoot(nodes)
    serialized = codec.serialize(result)
    assert data == serialized
