"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, 
return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # create tuples containing start, end, and profit
        intervals = sorted(zip(startTime, endTime, profit)) # sorted based on start time
        # create cache for caching
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            
            # dont include interval i
            res = dfs(i + 1)

            # include interval i
            j = i + 1
            # find j where start time > current intervals start time
            # use binary search (bisect) to avoid time limit exceeded
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res

        return dfs(0)

"""
this problem uses a recursive depth first search algorithm to find its solution.
the problem can be broken down as a decision tree with two options, use the current interval or dont.
we take our three arays and zip them together to create these intervals, which contain start, end, and profit.
we sort these intervals by start time so that we can go through them in an orderly fashion.
the basic algorithm has us deciding to exclude our current interval i, if so we call our dfs function on the next interval, i + 1.
if we chose to use our current interval, we have to find the next interval, j, which dosent overlap.
to find j we use bisect to perform a binary search (on a sorted list) to find the next value greater than our current intervals end time.
we set our res equal to the max of its current value (the value from not including i above) and our current profit plus dfs(j).
you'll notice we also make use of caching to avoid repeated work, this is just a hash table that acts as a visited set.
this solution runs in roughly O(nlogn) thanks to the binary search used in bisect.
"""