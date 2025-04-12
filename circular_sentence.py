class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        result = True
        words = sentence.split(" ")
        n = len(words)
        for i in range(n):
            j = (i - 1 + n) % n
            result = words[i][0] == words[j][-1]
            if not result:
                break

        return result
            

