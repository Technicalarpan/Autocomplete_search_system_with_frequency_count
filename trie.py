class TrieNode:
    def __init__(self):
        self.children = {} #it will store child nodes (key as character)
        self.is_end = False #True=> End of word otherwise false
        self.words = set()  # Store words passing through for autocomplete

class Trie:
    def __init__(self):
        self.root = TrieNode() #Rootnode

    def insert(self, word): 
        node = self.root #Start at root node
        for ch in word: #For each character in the word
            if ch not in node.children: #Condition check
                node.children[ch] = TrieNode() #New Trienode Created if already not present in node.children
            node = node.children[ch] #Move to child nood ( next node )
            node.words.add(word) #Add the whole word
        node.is_end = True

    def autocomplete(self, prefix):
        node = self.root #starts at root node
        for ch in prefix:
            if ch not in node.children:
                return []  # No match
            node = node.children[ch]
        return list(node.words) #Returns all word associated with prefix
