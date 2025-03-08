"""
Name: Koko Eating Bananas (#875)
URL: https://leetcode.com/problems/koko-eating-bananas/

Time Complexity: O(N * Log M)
Space Complexity: O(1)
"""

class Solution:
    # O(N)
    def timeRequiredAtRate(self, piles, rate):
        timeRequired = 0

        for pile in piles:
            timeRequired += math.ceil(pile / rate)

        return timeRequired


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        timeRequiredAtMidRate = 0

        # O(LogM)
        while left <= right:
            mid = (left + right) // 2

            timeRequiredAtMidRate = self.timeRequiredAtRate(piles, mid)

            if timeRequiredAtMidRate > h:
                left = mid + 1
            else:
                right = mid - 1

        return left