"""
Name: Replace Words (#648)
URL: https://leetcode.com/problems/replace-words/

Time Complexity:  O(NM + LK) [N: dict size; M: avg word len; L: sentence size; K: avg word len]
Space Complexity:O(NM + LK) [N: dict size; M: avg word len; L: sentence size; K: avg word len]
"""

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class DTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]  

        curr.end = True

    def get_root(self, word):
        curr = self.root

        for idx, ch in enumerate(word):
            if ch not in curr.children:
                return word

            curr = curr.children[ch]

            if curr.end:
                return word[:idx+1]

        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dt = DTrie()

        for word in dictionary:
            dt.insert(word)

        return " ".join([dt.get_root(word) for word in sentence.split(' ')])
        