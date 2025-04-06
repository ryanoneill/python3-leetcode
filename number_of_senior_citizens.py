from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # 0-9   phone number
        # 10    gender
        # 11-12 age
        # 13-14 seat allotment
        result = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                result += 1

        return result
