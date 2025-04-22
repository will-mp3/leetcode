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

"""