"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i : i[0])

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True 

"""
this solution is the simplest form of previous interval problems such as 435 and 56.
the idea is that we must return false if we find nay overlapping intervals.
how this can be done is by first sorting our list of intervals in increasing order by start time.
next we iterate through them and if at any point our current endpoint if greater than the next start point, they overlap.
if this is the case we return false.
this solution runs in O(nlogn).
"""