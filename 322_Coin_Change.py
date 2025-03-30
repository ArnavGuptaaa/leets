"""
Name: Coin Change (#322)
URL: https://leetcode.com/problems/coin-change/
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [float('inf')] * (amount + 1)

        """
        Time Complexity: O(M * N) [M: distinct states of remaining_amount]
        Space Complexity: O(M + M)
        """
        def memo_change(remaining_amount):
            if remaining_amount == 0:
                return 0

            if cache[remaining_amount] != float('inf'):
                return cache[remaining_amount]

            min_coins = float('inf')

            for coin in coins:
                if coin > remaining_amount:
                    continue

                min_coins = min(min_coins, 1 + memo_change(remaining_amount - coin))
            
            cache[remaining_amount] = min_coins
            return cache[remaining_amount]


        """
        Time Complexity: O(M * N) [M: distinct states of remaining_amount]
        Space Complexity: O(M)
        """
        def tab_change():
            cache[0] = 0

            for amt in range(1, amount + 1):
                for coin in coins:
                    if coin > amt:
                        continue

                    cache[amt] = min(cache[amt], 1 + cache[amt - coin])

            return cache[amount]

        # Memoized
        min_coins = memo_change(amount)
        return min_coins if min_coins != float('inf') else -1

        # Tabulated
        min_coins = tab_change()
        return min_coins if min_coins != float('inf') else -1