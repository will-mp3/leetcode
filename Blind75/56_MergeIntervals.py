"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][-1] # end value of most recent interval

            if start <= lastEnd: # start is overlapping with previous endpoint
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output

"""
to solve this problem we use similar logic to that of question 57 (detailed solution there).
essentially, we want to first ensure our interval list is sorted in increasing order.
with this set up we can iterate through our list of intervals, keeping track of the endpoint of our previous interval.
using this endpoint and the current endpoint we check to see if the previous endpoint and current start overlap (or are equal).
if so, we must merge them together by finding the max endpoint between the current and previous intervals and replacing it.
if there is no overlap, simply append the current interval and continue.
this solution runs in O(nlogn) 
"""