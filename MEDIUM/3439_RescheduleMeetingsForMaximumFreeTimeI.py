"""
You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.

You are also given two integer arrays startTime and endTime, each of length n. 
These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.

The relative order of all the meetings should stay the same and they should remain non-overlapping.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event.
"""

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        prefixSum = [0] * (n + 1)
        res = 0

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + (endTime[i] - startTime[i])
        
        print(prefixSum)
        
        for i in range(k - 1, n):
            right = eventTime if i == n - 1 else startTime[i + 1]
            left = 0 if i == k - 1 else endTime[i - k]
            res = max(res, right - left - (prefixSum[i + 1] - prefixSum[i - k + 1]))

        return res

"""
this code defines a class Solution with a method maxFreeTime that calculates the maximum amount of free time possible after rearranging meetings during an event.
It uses a prefix sum array to efficiently compute the total duration of meetings and iterates through possible meeting arrangements to find the maximum free time.
The method considers the constraints of rescheduling meetings while maintaining their order and non-overlapping nature, and returns the maximum free time achievable.
Time Complexity: O(n)
Space Complexity: O(n)
where n is the number of meetings.
This solution efficiently computes the maximum free time by leveraging prefix sums and iterating through the meetings,
ensuring that the solution is optimal and runs in linear time relative to the number of meetings.
"""