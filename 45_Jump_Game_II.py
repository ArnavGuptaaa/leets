"""
Name: Jump Game II (#45)
URL: <Add question link here>
"""

class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def greedy_soln(self, arr):
        N = len(arr)

        if N == 1:
            return 0

        if arr[0] == 0:
            return -1

        max_reach = 0
        last_index = 0

        jumps = 0

        for idx in range(len(arr)):
            max_reach = max(max_reach, idx + arr[idx])

            if idx == last_index:
                last_index = max_reach
                jumps += 1

                if max_reach >= N - 1:
                    return jumps

        return jumps


    """
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    def dynamic_soln(self, arr):
        cache = {}
	    
        def dp(idx):
            if idx in cache:
                return cache[idx]
	            
            if idx >= len(arr) - 1:
                return 0
	            
            min_jumps = float('inf')

            for i in range(idx + 1, min(len(arr), idx + arr[idx] + 1)):
                min_jumps = min(min_jumps, 1 + dp(i))

            cache[idx] = min_jumps
                
            return cache[idx]

        min_jumps = dp(0) 
        return min_jumps if min_jumps != float('inf') else -1

    def jump(self, arr):
        # return self.dynamic_soln(arr)
        return self.greedy_soln(arr)