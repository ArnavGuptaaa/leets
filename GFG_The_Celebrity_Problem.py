"""
Name: The Celebrity Problem (#GFG)
URL: https://www.geeksforgeeks.org/problems/the-celebrity-problem/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def celebrity(self, mat):
        top = 0
        bottom = len(mat) - 1
        
        while top < bottom:
            if mat[top][bottom]:
                top += 1
            elif mat[bottom][top]:
                bottom -= 1
            else:
                top += 1
                bottom -= 1
    
        if top > bottom:
            return -1
            
        for idx in range(len(mat)):
            if idx == top:
                continue
                
            if (
                mat[top][idx] != 0 or 
                mat[idx][top] != 1  
            ):
                return -1
                
        return top