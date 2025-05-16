from typing import List

class Solution:
    def are_close(self, word1: str, word2: str) -> bool:
        result = True
        count = 0
        m = len(word1)
        n = len(word2)
        if m != n:
            result = False
        else:
            for l1, l2 in zip(word1, word2):
                if l1 != l2:
                    count += 1
                    if count > 1:
                        result = False
                        break
        return result

    # TODO: Massive room for improvement here on list concatenation.
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        cache = {}
        def worker(previous: int, index: int) -> List[int]:
            results = []
            if index < n:
                key = (previous, index)
                if key not in cache:
                    if previous == -1:
                        option_one = [index]
                        option_one.extend(worker(index, index+1))
                        option_two = worker(previous, index+1)
                        if len(option_one) >= len(option_two):
                            results = option_one
                        else:
                            results = option_two
                    else:
                        previous_group = groups[previous]
                        current_group  = groups[index]

                        previous_word = words[previous]
                        current_word = words[index]
                        if previous_group == current_group:
                            results = worker(previous, index+1)
                        elif self.are_close(previous_word, current_word):
                            option_one = [index]
                            option_one.extend(worker(index, index+1))
                            option_two = worker(previous, index+1)
                            if len(option_one) >= len(option_two):
                                results = option_one
                            else:
                                results = option_two
                        else:
                            results = worker(previous, index+1)
                    cache[key] = results
                results = cache[key]
            return results

        indices = worker(-1, 0)
        results = list(map(lambda i: words[i], indices))
        return results
