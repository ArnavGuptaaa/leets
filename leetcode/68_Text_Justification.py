"""
Name: Text Justification (#68)
URL: https://leetcode.com/problems/text-justification/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        
        line = []
        line_char_count = 0
        
        for idx, word in enumerate(words):
            if line_char_count + len(line) + len(word) > maxWidth:

                spaces = (maxWidth - line_char_count) // max(1, len(line) - 1)
                remainder = (maxWidth - line_char_count) % max(1, len(line) - 1)

                for line_idx in range(max(1, len(line) - 1)):
                    line[line_idx] += " " * spaces

                    if remainder:
                        line[line_idx] += " "
                        remainder -= 1
            
                output.append("".join(line))

                line = []
                line_char_count = 0

            line.append(word)
            line_char_count += len(word)

        if line:
            output.append(" ".join(line) + " " * (maxWidth - (line_char_count + len(line) - 1)))

        return output