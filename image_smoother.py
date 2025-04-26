from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0

                # upper left
                if i > 0 and j > 0:
                    total += img[i-1][j-1]
                    count += 1

                # upper center
                if i > 0:
                    total += img[i-1][j]
                    count += 1

                # upper right
                if i > 0 and j < n-1:
                    total += img[i-1][j+1]
                    count += 1

                # left
                if j > 0:
                    total += img[i][j-1]
                    count += 1

                # center
                total += img[i][j]
                count += 1

                # right
                if j < n-1:
                    total += img[i][j+1]
                    count += 1

                # bottom left
                if i < m-1 and j > 0:
                    total += img[i+1][j-1]
                    count += 1

                # bottom center
                if i < m-1:
                    total += img[i+1][j]
                    count += 1

                # bottom right
                if i < m-1 and j < n-1:
                    total += img[i+1][j+1]
                    count += 1

                value = total // count
                result[i][j] = value

        return result


