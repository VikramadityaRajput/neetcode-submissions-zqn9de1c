class TrieNode:
    def __init__(self):
        self.children = {} #map for all the children
        self.end = False #for the search function whether its the end of not

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children: # you either add it or it already exists
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True
    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True and cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
        