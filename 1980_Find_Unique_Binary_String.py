"""
Name: Find Unique Binary String (#1980)
URL: https://leetcode.com/problems/find-unique-binary-string/

Time Complexity: O(N * 2^N)  # This N factor can be reduced with converting nums to set
Space Complexity: O(N) 
"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        def backtrack(idx, path):
            if idx == len(nums):
                bit_string = "".join(path)

                if bit_string not in nums:
                    return bit_string

                return None

            for bit in ["0", "1"]:
                path.append(bit)
                res = backtrack(idx + 1, path)
                
                if res: return res

                path.pop()

        return backtrack(0, [])