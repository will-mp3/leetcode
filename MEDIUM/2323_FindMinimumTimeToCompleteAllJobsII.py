"""
You are given two 0-indexed integer arrays jobs and workers of equal length, 
where jobs[i] is the amount of time needed to complete the ith job, and workers[j] is the amount of time the jth worker can work each day.

Each job should be assigned to exactly one worker, such that each worker completes exactly one job.

Return the minimum number of days needed to complete all the jobs after assignment.
"""

class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        # brute force
        n = len(jobs)
        jobs.sort()
        workers.sort()
        res = float("-inf")

        for i in range(n):
            if jobs[i] % workers[i] == 0:
                res = max(res, jobs[i] // workers[i])
            else:
                res = max(res,1 + jobs[i] // workers[i])

        return res

"""
this solution takes advantage of the fact that both arrays are of equal lenght.
we know that since we are looking for the minimum, the nth fastest job should go to the worker with the nth amount of time.
this allows for our quickest job to go to our worker with the least hours and vice verse.
to accomplish this we begin by sorting our lists, this allows us to hit those 1 through n - 1 values in order.
we iterate through both lists and check each time if there is a remainder when jobs[i] is divided by workers[i].
if there is a remainder we have to add 1 to our computed value to account for the extra day required due to leftover time.
we return the max of our current res and the newly calculated one for each index, according to the above condition.
this solution runs in O(n log n) time due to the use of the sort function on both arrays.
"""