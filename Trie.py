class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.endsWith = 0
        self.countPrefix = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.countPrefix+=1
        node.endsWith += 1
        node.is_end = True

    def search(self,s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self,s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
    
    def wordsEndsWith(self,word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.endsWith

    def countWords(self,word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.countPrefix

trie = Trie()
trie.insert("apple")
trie.insert("apple")
trie.insert("app")
trie.insert("app")
print(trie.search("apple"))
print(trie.search("ap"))
print(trie.startsWith("appl"))
print(trie.startsWith("app"))
print(trie.startsWith("apz"))
print(trie.wordsEndsWith("app"))
print(trie.countWords("ap"))