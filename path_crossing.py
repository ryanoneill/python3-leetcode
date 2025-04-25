class Solution:
    def isPathCrossing(self, path: str) -> bool:
        result = False
        seen = set()
        pos = (0, 0)
        seen.add(pos)

        for direction in path:
            x, y = pos
            match direction:
                case "N":
                    pos = (x, y - 1)
                case "S":
                    pos = (x, y + 1)
                case "E":
                    pos = (x + 1, y)
                case "W":
                    pos = (x - 1, y)
            if pos in seen:
                result = True
                break
            else:
                seen.add(pos)

        return result
