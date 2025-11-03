"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.
"""

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n, sum_ = len(colors), 0
        i = 1
        while i < n:
            maxi = 0
            while i < n and colors[i] == colors[i - 1]:
                sum_ += neededTime[i - 1]
                maxi = max(maxi, neededTime[i - 1])
                i += 1
            sum_ += neededTime[i - 1]
            maxi = max(maxi, neededTime[i - 1])
            if maxi != 0:
                sum_ -= maxi
            i += 1
        return sum_

"""
This solution iterates through the string of balloon colors, identifying consecutive balloons of the same color. 
For each group of consecutive balloons with the same color, it calculates the total time needed to remove all but the one with the maximum removal time, which is kept. 
The total removal time is accumulated and returned at the end.
The time complexity of this solution is O(N), where N is the length of the colors string.
"""