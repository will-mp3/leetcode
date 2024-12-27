"""
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        
        return res

"""
this solution is solved in a similar fashion to other interval problems.
the first thing we want to do is sort the list of intervals in increasing order.
once sorted we iterate through the list, keeping track of the amount of intervals deleted (solution) and the previous endpoint.
to check if an interval is overlapping, we see if the current start is less than previous end.
if so we add 1 to our result and simulate the intervals removal by making the new previous end the min between the current and previous end.
if they are not overlapping simply update the previous end and continue.
this solution runs in O(nlogn), n for iterating and logn for sorting.
"""