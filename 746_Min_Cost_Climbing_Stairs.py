"""
Name: Min Cost Climbing Stairs (#746)
URL: https://leetcode.com/problems/min-cost-climbing-stairs/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * (len(cost) + 1)

        # ===
        def min_cost_memoized(start):
            if start >= len(cost):
                return 0

            if cache[start] != -1:
                return cache[start]

            current_cost = min(min_cost_memoized(start + 1), min_cost_memoized(start + 2)) + cost[start]

            cache[start] = current_cost

            return current_cost

        # ===
        def min_cost_tabulated():
            cache[0] = 0
            cache[1] = 0

            for idx in range(2, len(cost) + 1):
                cache[idx] = min(
                    cost[idx - 1] + cache[idx - 1],
                    cost[idx - 2] + cache[idx - 2],
                )

            return cache[len(cost)]
        
        # ===
        # return min(
        #     min_cost_memoized(0),
        #     min_cost_memoized(1)
        # )

        return min_cost_tabulated()
        