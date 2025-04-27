from typing import List

class Solution:
    def to_time_value(self, event: str) -> int:
        hours, minutes = event.split(":")
        result = int(hours) * 60 + int(minutes)
        return result

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1_start = self.to_time_value(event1[0])
        event1_end = self.to_time_value(event1[1])
        event2_start = self.to_time_value(event2[0])
        event2_end = self.to_time_value(event2[1])

        # Event 1 starts before Event 2
        # - Event 2 starts before or when Event 1 ends
        # Event 2 starts before Event 1
        # - Event 1 starts before or when Event 2 ends

        result = event1_start <= event2_start and event2_start <= event1_end
        result = result or (event2_start <= event1_start and event1_start <= event2_end)

        return result
