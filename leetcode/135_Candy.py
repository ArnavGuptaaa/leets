"""
Name: Candy (#135)
URL: https://leetcode.com/problems/candy/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for idx in range(1, len(ratings)):
            prev_rating = ratings[idx - 1]
            curr_rating = ratings[idx]

            if curr_rating > prev_rating:
                candies[idx] = candies[idx - 1] + 1

        result = candies[len(ratings) - 1]

        for idx in range(len(ratings) - 2, -1, -1):
            next_rating = ratings[idx + 1]
            curr_rating = ratings[idx]

            if curr_rating > next_rating and candies[idx] <= candies[idx + 1]:
                candies[idx] = candies[idx + 1] + 1

            result += candies[idx]

        return result