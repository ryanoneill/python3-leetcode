from typing import List


class TrieNode:
    def __init__(self, value: str) -> None:
        self.value = value
        self.ends = False
        self.children = {}
        self.words = []


class Trie:
    def __init__(self) -> None:
        self.words = []
        self.root = TrieNode("*")

    def insert(self, word: str) -> None:
        self.words.append(word)
        index = len(self.words) - 1
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
            current = current.children[letter]
            if len(current.words) < 3:
                current.words.append(index)
        current.ends = True

    def search(self, word: str) -> List[List[str]]:
        n = len(word)
        results = [[] for _ in range(n)]
        current = self.root
        for i, letter in enumerate(word):
            if letter in current.children:
                current = current.children[letter]
                for j in current.words:
                    results[i].append(str(self.words[j]))
            else:
                break
        return results


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.insert(product)
        results = trie.search(searchWord)
        return results
