class TrieNode:
    def __init__(self, value: str) -> None:
        self.value = value
        self.children = {}
        self.ends = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("*")

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
            current = current.children[letter]
        current.ends = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        return current.ends

    def startsWith(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        return True

