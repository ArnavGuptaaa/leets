"""
Link : https://leetcode.com/discuss/post/6244752/google-l3-interview-experience-questions-2utz/

Question:
You are given an array of strings songs, where each string represents the songs in the order they should be played for a person. 
Each string contains the list of songs that a particular person wants to hear, in the order they wish to hear them.

There are n people, and each person has their own specific order in which they want the songs to be played.
We need to determine if there exists a valid order in which all the songs can be played that satisfies every person's song order. 
If such a valid order exists, return the order. If no valid order exists, return an empty list.
"""

class Solution:
    def get_music_order(n, songs):
        def topological_order(node, node_states, music_order):
            if node_states[node] == 2:
                return True

            if node_states[node] == 1:
                return False

            node_states[node] = 1

            for nei in adj[node]:
                if not topological_order(nei, node_states, music_order):
                    return False

            node_states[node] = 2
            music_order.append(node)

            return True

        # Prepare adj map
        adj = {}
        for person in songs:
            for idx, song in enumerate(person):
                if song not in adj:
                    adj[song] = set()

                if idx < len(person) - 1:
                    adj[song].add(person[idx + 1])

        music_order = []

        """
        0 : unvisited,
        1 : visiting,
        2 : visited
        """
        node_states = {node: 0 for node in adj.keys()}

        for node in adj.keys():
            
            if not topological_order(node, node_states, music_order):
                return []
        
        return music_order[::-1]

# ===
from collections import deque

class Solution:
    def get_music_order(n, songs):
        def kahns_order(adj):
            # Prepare indegrees
            indegrees =  {node: 0 for node in adj.keys()}

            for node in adj.keys():
                for nei in adj[node]:
                    indegrees[nei] += 1

            # Prepare node queue
            node_queue = deque()

            for node in indegrees.keys():
                if indegrees[node] == 0:
                    node_queue.append(node)

            # Relax Edges
            order = []
            while node_queue:
                node = node_queue.popleft()
                order.append(node)

                for nei in adj[node]:
                    indegrees[nei] -= 1

                    if  indegrees[nei] == 0:
                        node_queue.append(nei)

            if len(order) != len(adj.keys()):
                return []

            return order


        # Prepare adj map
        adj = {}
        for person in songs:
            for idx, song in enumerate(person):
                if song not in adj:
                    adj[song] = set()

                if idx < len(person) - 1:
                    adj[song].add(person[idx + 1])

        return kahns_order(adj)