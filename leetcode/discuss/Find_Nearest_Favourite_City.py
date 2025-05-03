"""
Link : https://leetcode.com/discuss/post/5720580/google-swe-2-l3-bangalorehyd-aug-24-by-a-7kr8/


You are given n cities numbered from 1 to n, and a list of roads where each road is represented as a triplet [u, v, time], indicating that there is a bidirectional road between city u and city v that takes time units to travel.

You are also given:
a list of favoriteCities, containing a subset of city numbers,
and a source city src.

Your task is to return the favorite city that can be reached from the source city src in the minimum time.
If there are multiple favorite cities with the same minimum travel time, return the one with the smallest city number.
If none of the favorite cities are reachable from src, return -1.
"""

from heapq import heappush, heappop

class Solution:
    def nearestFavoriteCity(self, n, roads, favoriteCities, src):
        adj = {node: set() for node in range(1, n + 1)}

        for source, destination, time in roads:
            adj[source].add((destination, time))
            adj[destination].add((source, time))

        times = [float('inf')] * (n + 1)
        min_heap = [(0, src)]
        times[src] = 0
        times[0] = 0
        
        result = (float('inf'), n + 1)

        while min_heap:
            current_time, current_node = heappop(min_heap)

            if current_node in favoriteCities and (current_time < result[0] or (current_time == result[0] and current_node < result[1])):
                result = (current_time, current_node)

            if current_time > times[node]:
                continue

            for nei, required_time in adj[current_node]:
                if current_time + required_time < times[nei]:
                    times[nei] = current_time + required_time
                    heappush(min_heap, (times[nei], nei))

        return result[1] if result[0] != float('inf') else -1




        
