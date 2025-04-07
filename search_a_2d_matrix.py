from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if target < matrix[0][0]:
            return False

        row = -1

        left = 0
        right = m - 1
        while left <= right:
            mid = left + (right - left) // 2
            num = matrix[mid][0]
            if num == target:
                return True
            elif num < target:
                row = mid
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            num = matrix[row][mid]
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
