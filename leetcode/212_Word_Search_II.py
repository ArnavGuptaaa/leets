"""
Name: Word Search II (#212)
URL: https://leetcode.com/problems/word-search-ii/

Time Complexity: O(M * N * 4^L + W * L)
Space Complexity: O(W * L + N * M)
"""

class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def preprocess_words(self, words):
        for word in words:
            curr = self.root

            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                
                curr = curr.children[ch]

            curr.word = word
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()

        # ===
        def dfs(row, col, t_node):
            ch = board[row][col]

            if ch not in t_node.children:
                return

            t_node = t_node.children[ch]

            if t_node.word:
                result.add(t_node.word)

            board[row][col] = '~'

            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1],
            ]

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if (
                    0 <= new_row < len(board) and
                    0 <= new_col < len(board[0]) and
                    board[new_row][new_col] != '~'
                ):
                    dfs(new_row, new_col, t_node)

            board[row][col] = ch

        # ===
        self.preprocess_words(words)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in self.root.children:
                    dfs(row, col, self.root)

        return list(result)