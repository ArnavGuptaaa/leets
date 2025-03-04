"""
Name: Task Scheduler (#621)
URL: https://leetcode.com/problems/task-scheduler/

Time Complexity: O(N * LogN)
Space Complexity: O(N)
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get frequency
        freqMap = {}

        # O(N)
        for task in tasks:
            freqMap[task] = freqMap.get(task, 0) + 1

        # We want the highest frequency job to be dealt first
        # Use a max heap

        # [(-frequency, task)]
        # O(N)
        tasks = [(-1 * freqMap[task], task) for task in freqMap.keys()]

        # O(N)
        heapify(tasks)

        # Dealing means enqueue it in our execution queue
        # Stores (task, freq, completionTime)
        executionQueue = deque()

        # Dequeueing operation would be done when current time == the execution time of front
        # O(N)
        currentTime = 0
        while executionQueue or tasks:
            currentTime += 1

            # If task exists in heap, we put it in execution queue
            if tasks:
                # O(LogN)
                frequency, task = heappop(tasks)

                frequency = -1 * frequency
                completionTime = currentTime + n

                if frequency > 1:
                    executionQueue.append((task, frequency - 1, completionTime))
            
            # If the frontmost job can be processed, we process it
            # Then make it available to be queued again
            if executionQueue and executionQueue[0][2] <= currentTime:
                task, frequency, _ = executionQueue.popleft()

                # O(LogN)
                heappush(tasks, (-1 * frequency, task))

        return currentTime