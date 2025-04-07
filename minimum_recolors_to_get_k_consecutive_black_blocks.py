class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        count = 0
        result = k

        for i in range(0, k):
            if blocks[i] == "W":
                count += 1
        result = count

        for i in range(k, n):
            if blocks[i - k] == "W":
                count -= 1
            if blocks[i] == "W":
                count += 1
            result = min(result, count)

        return result
