"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by start_i. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i 
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # not overlapping
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # not overlapping
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)

        return res

"""
this solution inserts the intervals using just one loop and a result array.
the way it works is for every interval, three conditions are checked:
first, is the largest value in our new interval smaller than the smallest value of the current interval?
if true, add the new interval and add the rest of the intervals following to result, every further interval is larger and wont overlap.
second, is the smallest value in the new interval larger and the largest value of the current interval?
if true, add the current interval because it is behind the new interval but dont add the new interval yet, it could still overlap in the future.
if neither of these are true, then our interval is overlapping and we must merge it with the current interval.
we do this by replacing the new interval with the minimum and maximum of the new interval and current interval's points.
if the first condition has not activated by the time the loop ends, append the new interval and return result.
this solution runs in O(n) linear time.
"""