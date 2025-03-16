"""
Name: Search Suggestions System (#1268)
URL: https://leetcode.com/problems/search-suggestions-system/

Time Complexity: O(N log N + NM)
Space Complexity: O(NM)
"""

# =========
class TrieNode:
    def __init__(self):
        # self.end = False
        self.children = {}
        self.suggestions = []

class STrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

            curr.suggestions.append(word)
            curr.suggestions.sort()

            if len(curr.suggestions) > 3:
                curr.suggestions.pop()
                
        # curr.end = True

    def get_suggestions(self, inp):
        curr = self.root
        result = []

        for ch in inp:
            if ch not in curr.children:
                result.extend([[]] * (len(inp) - len(result)))
                break

            curr = curr.children[ch]
            result.append(curr.suggestions)

        return result

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        st = STrie()

        for product in products:
            st.insert(product)

        return st.get_suggestions(searchWord)
