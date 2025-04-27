from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []

        current_time = 0
        for log in logs:
            match log.split(":"):
                case [id_str, "start", start_time_str]:
                    id = int(id_str)
                    start_time = int(start_time_str)
                    if stack:
                        diff = start_time - current_time
                        running_id = stack[-1][0]
                        result[running_id] += diff
                    stack.append((id, start_time))
                    current_time = start_time
                case [id_str, "end", end_time_str]:
                    id = int(id_str)
                    end_time = int(end_time_str)
                    if stack:
                        diff = end_time - current_time + 1
                        running_id = stack[-1][0]
                        result[running_id] += diff
                        stack.pop()
                    current_time = end_time + 1

        return result
