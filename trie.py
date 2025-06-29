class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.words = set()  # Store words passing through for autocomplete

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.words.add(word)
        node.is_end = True

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []  # No match
            node = node.children[ch]
        return list(node.words)
