"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

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

"""