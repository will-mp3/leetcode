"""
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.
"""

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra = sum(batteries[:-n])
        live = batteries[-n:]

        for i in range(n - 1):
            if extra // (i + 1) < live[i + 1] - live[i]:
                return live[i] + extra // (i + 1)
            extra -= (i + 1) * (live[i + 1] - live[i])
        
        return live[-1] + extra // n

"""
This solution first sorts the battery capacities and separates the largest n batteries to power the n computers. 
It then calculates the total extra capacity from the remaining batteries. 
The algorithm iterates through the n largest batteries, checking if the extra capacity can equalize the current battery to the next one. 
If it can, it adjusts the extra capacity accordingly; 
if not, it calculates the maximum possible runtime based on the current battery level and the remaining extra capacity. 
Finally, if all batteries can be equalized, it returns the maximum runtime based on the last battery and any remaining extra capacity.  
"""