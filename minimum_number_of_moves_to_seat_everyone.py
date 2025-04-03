from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result = 0
        seats.sort()
        students.sort()

        for seat, student in zip(seats, students):
            result += abs(seat - student)

        return result
