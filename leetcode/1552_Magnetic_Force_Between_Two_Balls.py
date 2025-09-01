"""
Name: Magnetic Force Between Two Balls (#1552)
URL: <Add LeetCode link here>

Time Complexity: O(N*LogN + N*LogD)
Space Complexity: O(1)
"""

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # ===
        def is_good_distance(distance):
            start = position[0]
            count = 1

            for pos in position:
                if pos - start >= distance:
                    count += 1
                    start = pos

                    if count == m:
                        return True

            return False

        # ===
        position.sort()

        start, end = 1, position[-1] - position[0]
        res = -1

        while start <= end:
            mid = (start + end) >> 1

            if is_good_distance(mid):
                res = mid
                start = mid + 1
            else:
                end = mid - 1
        
        return res