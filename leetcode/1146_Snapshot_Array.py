"""
Name: Snapshot Array (#1146)
URL: https://leetcode.com/problems/snapshot-array/

Time Complexity: O(S) [S : Number of snapshots taken]
Space Complexity: O(N * S)
"""

class SnapshotArray:

    def __init__(self, length: int):
        self.version_id = 0

        # every index in array is {version => value_at_version}
        self.snapshot_arr = [{0: 0} for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        self.snapshot_arr[index][self.version_id] = val        


    def snap(self) -> int:
        prev_id = self.version_id
        self.version_id += 1

        return prev_id
        

    def get(self, index: int, snap_id: int) -> int:
        while snap_id not in self.snapshot_arr[index]:
            snap_id -= 1

        return self.snapshot_arr[index][snap_id]