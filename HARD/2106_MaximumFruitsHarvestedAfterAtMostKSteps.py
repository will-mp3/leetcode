"""
Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts amounti fruits at the position positioni. 
fruits is already sorted by positioni in ascending order, and each positioni is unique.

You are also given an integer startPos and an integer k. Initially, you are at the position startPos. 
From any position, you can either walk to the left or right. 
It takes one step to move one unit on the x-axis, and you can walk at most k steps in total. 
For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.

Return the maximum total number of fruits you can harvest.
"""

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = total = res = 0
        for right in range(len(fruits)):
            total += fruits[right][1]
            while left <= right and min(
                abs(startPos - fruits[left][0]) + fruits[right][0] - fruits[left][0],
                abs(startPos - fruits[right][0]) + fruits[right][0] - fruits[left][0]
            ) > k:
                total -= fruits[left][1]
                left += 1
            res = max(res, total)
        return res

"""

"""