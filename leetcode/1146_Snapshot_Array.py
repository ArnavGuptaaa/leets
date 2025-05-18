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


"""
Bsearch solution
"""

class SnapshotArray:

    def __init__(self, length: int):
        self.version_id = 0

        # every index in array is [[snap_id, value]]
        self.snapshot_arr = [[[0, 0]] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        if self.snapshot_arr[index][-1][0] == self.version_id:
            self.snapshot_arr[index][-1][1] = val
        else:
            self.snapshot_arr[index].append([self.version_id, val])


    def snap(self) -> int:
        prev_id = self.version_id
        self.version_id += 1

        return prev_id
        
    # Log(M) per call
    def get(self, index: int, snap_id: int) -> int:
        snap_id_list = self.snapshot_arr[index]

        start = 0
        end = len(snap_id_list) - 1
        
        result = 0

        while start <= end:
            mid = (start + end) >> 1

            if snap_id == snap_id_list[mid][0]:
                result = mid
                break
            
            if snap_id_list[mid][0] < snap_id:
                result = mid
                start = mid + 1
            else:
                end = mid - 1

        return snap_id_list[result][1]