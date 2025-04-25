from typing import List


class SegmentTree:
    def __init__(self, value: int, left: int, right: int) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.left_tree = None
        self.right_tree = None

    def query(self, left: int, right: int) -> int:
        result = 0
        if self.left == left and self.right == right:
            result = self.value
        else:
            mid = self.left + (self.right - self.left) // 2
            if left > mid:
                if self.right_tree:
                    result = self.right_tree.query(left, right)
            elif right <= mid:
                if self.left_tree:
                    result = self.left_tree.query(left, right)
            else:
                if self.left_tree and self.right_tree:
                    result = self.left_tree.query(left, mid) + self.right_tree.query(
                        mid + 1, right
                    )
        return result

    @staticmethod
    def build(nums: List[int]) -> "SegmentTree":
        n = len(nums)
        return SegmentTree._build(nums, 0, n - 1)

    @staticmethod
    def _build(nums: List[int], left: int, right: int) -> "SegmentTree":
        if left == right:
            num = nums[left]
            return SegmentTree(num, left, right)
        else:
            mid = left + (right - left) // 2

            result = SegmentTree(0, left, right)
            result.left_tree = SegmentTree._build(nums, left, mid)
            result.right_tree = SegmentTree._build(nums, mid + 1, right)
            result.value = result.left_tree.value + result.right_tree.value

            return result
