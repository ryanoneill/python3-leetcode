from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        squares = sum(students)
        circles = n - squares

        eaten = 0
        for sandwich in sandwiches:
            if sandwich == 1:
                if squares > 0:
                    squares -= 1
                    eaten += 1
                else:
                    break
            else:
                if circles > 0:
                    circles -= 1
                    eaten += 1
                else:
                    break

        result = n - eaten
        return result
