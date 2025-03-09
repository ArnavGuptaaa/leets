"""
Name: Coin Change (#322)
URL: https://leetcode.com/problems/coin-change/

Time Complexity: O(M * N) [M: distinct states of remaining_amount]
Space Complexity: O(N)
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        # ===
        def min_number_of_coins(remaining_amount):
            if remaining_amount in cache:
                return cache[remaining_amount]

            if remaining_amount < 0:
                return float('inf')

            if remaining_amount == 0:
                return 0

            min_coins = float('inf')

            for coin in coins:
                num_coins = 1 + min_number_of_coins(remaining_amount - coin)

                min_coins = min(num_coins, min_coins)

            cache[remaining_amount] = min_coins
            return min_coins
        
        # ===
        num_changes = min_number_of_coins(amount)
        return num_changes if num_changes != float('inf') else -1