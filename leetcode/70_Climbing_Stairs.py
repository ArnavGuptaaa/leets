"""
Name: Climbing Stairs (#70)
URL: https://leetcode.com/problems/climbing-stairs/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 1)

        # ===
        def distinct_ways_memoized(step):
            if step <= 1:
                return 1

            if cache[step] != -1:
                return cache[step]

            ways = distinct_ways_memoized(step - 1) + distinct_ways_memoized(step - 2)

            cache[step] = ways

            return ways
        
        # ===
        def distinct_ways_tabulated(step):
            cache[0] = 1
            cache[1] = 1

            for idx in range(2, step + 1):
                cache[idx] = cache[idx - 1] + cache[idx - 2]

            return cache[step]

        # ===
        # return distinct_ways_memoized(n)
        return distinct_ways_tabulated(n)