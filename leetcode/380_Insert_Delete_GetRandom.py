"""
Name: Insert Delete GetRandom (#380)
URL: https://leetcode.com/problems/insert-delete-getrandom-o1/

Time Complexity: O(1)
Space Complexity: O(N)
"""

class RandomizedSet:
    def __init__(self):
        self.num_map = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False

        self.num_map[val] = len(self.num_list)
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_map:
            return False

        # Get the index which needs to be erased
        idx = self.num_map[val]

        # Move the last element to the previously fetched index
        self.num_list[idx] = self.num_list[-1]

        # Update the mapping for the moved element
        self.num_map[self.num_list[idx]] = idx

        # Pop the last element
        self.num_list.pop()

        # Delete the element from mapping
        del self.num_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)
