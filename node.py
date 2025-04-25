from typing import List, Optional


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ) -> None:
        if children is None:
            children = []
        self.val = val
        self.children = children
