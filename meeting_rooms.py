from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        current = 0
        result = True
        for interval in intervals:
            start, end = interval
            if current > start:
                result = False
                break
            else:
                current = end

        return result
