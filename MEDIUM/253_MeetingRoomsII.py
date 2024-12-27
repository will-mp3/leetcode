"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]: # start time less than end time
                s += 1
                count += 1
            else: # start time greater than or equal to end time
                e += 1
                count -= 1
            res = max(res, count)

        return res

"""
to solve this version of meeting rooms, we need to find the maximum amount of overlapping intervals at a given time.
to achieve this we can use an algorithm comparing start and end times.
if we sort the start and end times, and count the amount of start times that happen compared to end times, we get our result.
the way this algorithm works in code is by sorting both start and end times in separate arrays.
we then iterate through these arrays and compare the start and end times (starting at position zero).
if the current start time is less than the current end time we add one to our count, 
this shows that a meeting has started and before one has ended.
we then increment our start time and count by 1.
if our start time is greater than or equal to our end time, we increment our end time by one and decrement count by 1.
this shows a meeting ending.
with each iteration we update the max to see if its gotten larger.
this solution runs in O(nlogn) linear time.
"""