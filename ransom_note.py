class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = True

        ransomNoteCounts = {}
        for letter in ransomNote:
            if letter in ransomNoteCounts:
                ransomNoteCounts[letter] += 1
            else:
                ransomNoteCounts[letter] = 1
        magazineCounts = {}
        for letter in magazine:
            if letter in ransomNoteCounts:
                if letter in magazineCounts:
                    magazineCounts[letter] += 1
                else:
                    magazineCounts[letter] = 1

        for key, value in ransomNoteCounts.items():
            if key not in magazineCounts:
                result = False
                break
            elif magazineCounts[key] < value:
                result = False
                break

        return result
