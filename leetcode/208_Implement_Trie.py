"""
Name: Implement Trie (#208)
URL: https://leetcode.com/problems/implement-trie-prefix-tree/

Time Complexity: O(N)
Space Complexity: O(M*N) [M : words; N: Average Length]
"""

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            
            curr = curr.children[ch]
        
        curr.end = True
    
    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]

        return True