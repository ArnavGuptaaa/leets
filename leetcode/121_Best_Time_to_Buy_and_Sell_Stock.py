"""
Name: Best Time to Buy and Sell Stock (#121)
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minSoFar = prices[0]  

        for idx in range(1, len(prices)):
            localProfit = prices[idx] - minSoFar
            res = max(localProfit, res)

            minSoFar = min(minSoFar, prices[idx])

        return res