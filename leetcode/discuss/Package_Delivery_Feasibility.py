"""
Link : https://leetcode.com/discuss/post/6352084/google-l4-phone-screening-round-by-anony-aa15/

Question : 
You are given an origin airport s, a destination airport t, and a list of flights.
Each flight is represented by a tuple of four elements: (departure_airport, arrival_airport, departure_time, arrival_time).
A package starts at the origin airport s at time 0. 
It can only be transferred to another flight after it has arrived at an airport, 
meaning it can only board a flight if the flight's departure_time is greater than or equal to the time the package arrived at that airport.

Example:
s = "NYC"
t = "SFO"
flights = [
    ("NYC", "LAX", 0, 4),
    ("LAX", "SFO", 5, 7)
]

Output : True
"""
from collections import deque
class Solution:
    def __init__(self):
        pass

    def can_deliver_package(self, src, dst, flights):
        # Create Adjacency List
        adj = {}

        for s, d, departure, arrival in flights:
            if s not in adj:
                adj[s] = set()

            adj[s].add((d, departure, arrival))
        
        # BFS Traversal
        queue = deque()
        queue.append((src, 0))

        while queue:
            source, time = queue.popleft()

            if source == dst:
                return True

            if source in adj:
                for destination, departure, arrival in adj[source]:
                    if time <= departure:
                        queue.append((destination, arrival))

        return False


# Test

sol = Solution()

test_cases = [
    ["NYC", "SFO", [("NYC", "LAX", 0, 4), ("LAX", "SFO", 5, 7)], True],
    ["NYC", "SFO", [("NYC", "LAX", 0, 4), ("LAX", "SFO", 3, 5)], False],
    ["A", "B", [("A", "B", 0, 2)], True],
    ["A", "B", [], False],
    ["A", "D", [
        ("A", "B", 0, 1),
        ("B", "C", 2, 3),
        ("C", "A", 4, 5),
        ("C", "D", 6, 7)
    ], True],
    ["X", "Y", [("A", "B", 0, 1), ("B", "C", 2, 3)], False],
    ["A", "D", [
        ("A", "B", 0, 2),
        ("B", "D", 5, 6), 
        ("A", "C", 0, 1),
        ("C", "D", 1, 2)   
    ], True],
    ["A", "C", [("A", "B", 0, 2), ("B", "C", 2, 3)], True],
    ["A", "C", [("A", "B", 0, 5), ("B", "C", 3, 4)], False],
]

for case in test_cases:
    source, destination, flights, expected = case

    actual = sol.can_deliver_package(source, destination, flights)
    print(f'Expected: {expected}; Actual: {actual}\n===\n')
