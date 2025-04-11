"""
Name: Group Anagrams (#49)
URL: https://leetcode.com/problems/group-anagrams/

Time Complexity: O(N * M log M)  
Space Complexity: O(N * M)  
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        resDict = {}

        for s in strs:
            sortedCharArr = sorted(s)
            sortedStr = ''.join(sortedCharArr)

            if sortedStr in resDict:
                resDict[sortedStr].append(s)
            else:
                resDict[sortedStr] = [s]
            
        return list(resDict.values())