"""
Name: Meeting Rooms II (#253)
URL: https://leetcode.com/problems/meeting-rooms-ii/

Time Complexity: O(N log N)
Space Complexity: O(N)
"""

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Min heap to track the earliest end time
        ongoingMeetings = []

        # We would want to iterate the meetings chronologically
        # O(N * LogN)
        intervals.sort(key = lambda x: x.start)

        # O(N * LogN)
        for meeting in intervals:
            # If current meeting start time is greater than earliest meeting end time
            # We can schedule our meeting
            if len(ongoingMeetings) > 0 and meeting.start >= ongoingMeetings[0]:
                heapq.heappop(ongoingMeetings)
            
            # Schedule our meeting
            heapq.heappush(ongoingMeetings, meeting.end)

        return len(ongoingMeetings)