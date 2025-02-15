"""
Name: LRU Cache (#146)
URL: https://leetcode.com/problems/lru-cache/

Time Complexity: O(1)
Space Complexity: O(N)
"""

class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.cache = {}
        self.mostRecent = self.leastRecent = Node(-1, -1)

        self.mostRecent.prev = self.leastRecent
        self.leastRecent.next = self.mostRecent
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
        
        return node

    def insertNode(self, node):
        prevNode = self.mostRecent.prev
        nextNode = self.mostRecent

        node.next = nextNode
        nextNode.prev = node

        node.prev = prevNode
        prevNode.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            removedNode = self.removeNode(self.cache[key])
            self.insertNode(removedNode)

            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insertNode(self.cache[key])

        if len(self.cache) > self.capacity:
            leastRecentNode = self.leastRecent.next
            self.removeNode(leastRecentNode)

            del self.cache[leastRecentNode.key]