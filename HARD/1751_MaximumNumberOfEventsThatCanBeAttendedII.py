"""
You are given an array of events where events[i] = [startDayi, endDayi, valuei]. 
The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. 
Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.
"""

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        starts = [start for start, end, value in events]
        dp = [[-1] * n for _ in range(k + 1)]

        def dfs(cur_index, count):
            if count == 0 or cur_index == n:
                return 0
            if dp[count][cur_index] != -1:
                return dp[count][cur_index]

            # Find the nearest available event after attending event 0.

            next_index = bisect_right(starts, events[cur_index][1])
            dp[count][cur_index] = max(dfs(cur_index + 1, count), events[cur_index][2] + dfs(next_index, count - 1))
            return dp[count][cur_index]
        
        return dfs(0, k)

"""
this code defines a class Solution with a method maxValue that calculates the maximum sum of values from attending events, given constraints on the number of events and their timings. 
It uses dynamic programming and binary search to efficiently find the optimal solution.
The code sorts the events, initializes a DP table, and uses a recursive function with memoization to compute the maximum value. 
It uses binary search to find the next available event after attending a current event, ensuring that the solution is efficient even for larger inputs.
Time Complexity: O(n^2 * k)
Space Complexity: O(n * k)
where n is the number of events and k is the maximum number of events that can be attended.
"""