"""
Link : https://leetcode.com/discuss/post/6355995/google-l3-interview-experience-ghosted-b-f2ed/

Question : 
You are given n routers placed on a 2D Cartesian plane. Each router has a unique position (x, y). 
You are also given a source router and a destination router. 
Your task is to determine whether it is possible to reach the destination starting from the source, under the following constraints:

1. From the current router, you may move to a single adjacent router that:
    - Is within a maximum allowed distance threshold.
2. Once a router is visited, the previously visited router becomes inactive and can no longer be visited again.
"""

class Solution:
    def __init__(self):
        pass
    
    def get_euclidean_distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2

        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def canReachDestination(self, routers, source, destination, threshold):
        adj = {node:set() for node in range(len(routers))}

        # Prepare Adjacency List
        for idx in range(len(routers)):
            x1, y1 = routers[idx]

            for idx2 in range(len(routers)):
                if idx == idx2:
                    continue

                x2, y2 = routers[idx2]

                distance = self.get_euclidean_distance((x1, y1), (x2, y2))

                if distance <= threshold:
                    adj[idx].add(idx2)


        # Perform DFS from node
        visited = set()

        def dfs(node):
            if node == destination:
                return True
            
            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                if dfs(nei):
                    return True
                
            return False

        return dfs(source)


# Test
sol = Solution()
test_cases = [
    [
        [(0, 0), (1, 1), (2, 2), (3, 3)],  
        0,  
        3,  
        5,  
        True  
    ],
    [
        [(0, 0), (3, 4)],  
        0,  
        1,  
        5,  
        True  
    ],
    [
        [(0, 0), (2, 2), (4, 4), (6, 6), (8, 8)],  
        0,  
        4,  
        10,  
        True  
    ],
    [
        [(0, 0), (3, 5), (6, 8)],  
        0,  
        2,  
        2,  
        False  
    ],
    [
        [(0, 0), (1, 1), (2, 2)],  
        0,  
        0,  
        3,  
        True  
    ]
]

for case in test_cases:
    routers, source, destination, threshold, expected_return = case
    actual = sol.canReachDestination(routers, source, destination, threshold)
    
    print(f'''Expected: {expected_return}; Actual: {actual}
===\n''')
            
        