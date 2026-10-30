class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
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

trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))
print(trie.search("ap"))
print(trie.startsWith("appl"))
print(trie.startsWith("app"))
print(trie.startsWith("apz"))