"""
Link : https://leetcode.com/discuss/post/6386506/google-l3-phone-screen-by-anonymous_user-gjax/

Question:
A town is building a watchtower at a fixed location to monitor nearby houses. 
The watchtower can be built to any height ≥ 0. The horizontal surveillance range of the tower is equal to its height. 
Any house that lies within a circle centered at the watchtower (x₀, y₀) with radius equal to the height is considered under surveillance.

Each unit of height costs H units to build, and each house that comes under surveillance pays C units to the builder. 
Your task is to determine the maximum profit that can be achieved by choosing the optimal height for the watchtower.
"""

class Solution:
    def get_max_profit(self, houses, watchtower_location, height_cost, house_cost):

        def get_distance_from_watchtower(x, y):
            return ((watchtower_location[0] - x) ** 2 + (watchtower_location[1] - y) ** 2) ** 0.5

        
        house_distances = [get_distance_from_watchtower(x, y) for x, y in houses]
        house_distances.sort()

        max_profit = float('-inf')
        for idx, distance in enumerate(house_distances):
            profit = ((idx + 1) * house_cost) - (distance * height_cost)
            max_profit = max(max_profit, profit)

        return max_profit