"""
Name: Sliding Window Maximum (#239)
URL: https://leetcode.com/problems/sliding-window-maximum/

Time Complexity
deque_solution : O(N)
heap_solution : O(N * LogK)


Space Complexity
deque_solution : O(K)
heap_solution : O(K)
"""

class Solution:
    def deque_solution(self, nums, k):
        max_window = []
        dq = deque()

        for idx, num in enumerate(nums):
            # If we encounter a bigger number than end, update it.
            while dq and num > nums[dq[-1]]:
                dq.pop()

            dq.append(idx)

            # Ensure that front is always from within the window
            while dq and dq[0] < idx - k + 1:
                dq.popleft()

            # If window has grown over k, add max value
            if idx >= k - 1:
                max_window.append(nums[dq[0]])

        return max_window

    def heap_solution(self, nums, k):
        left = right = 0
        
        max_heap = []
        max_window = []

        while right < len(nums):
            heapq.heappush(max_heap, (-1 * nums[right], right))

            if right - left + 1 == k:
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)

                max_window.append(-1 * max_heap[0][0])

                left += 1

            right += 1
    
        return max_window

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return self.heap_solution(nums, k)
        return self.deque_solution(nums, k)