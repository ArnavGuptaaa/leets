"""
Name: Gas Station (#134)
URL: https://leetcode.com/problems/gas-station/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        remaining_gas = 0

        total_gas = 0
        total_cost = 0

        for idx in range(len(gas)):
            total_gas += gas[idx]
            total_cost += cost[idx]

            remaining_gas += gas[idx] - cost[idx]

            if remaining_gas < 0:
                start = idx + 1
                remaining_gas = 0

        if total_cost > total_gas:
            return -1

        return start