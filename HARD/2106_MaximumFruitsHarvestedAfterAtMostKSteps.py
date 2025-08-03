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
This code defines a solution to maximize the total number of fruits harvested from given positions on an infinite x-axis, considering movement constraints.
The `maxTotalFruits` method uses a two-pointer technique to efficiently calculate the maximum fruits that can be harvested within the allowed steps. 
It iterates through the list of fruits, maintaining a running total of fruits collected from the current range defined by the left and right pointers.
If the total distance from the starting position to the leftmost and rightmost positions exceeds k, it adjusts the left pointer to reduce the total until the condition is satisfied.
The maximum total is updated at each step, ensuring that the solution captures the optimal range of fruits that can be harvested.
The time complexity of this solution is O(n), where n is the number of fruit positions, as it processes each position at most twice (once by each pointer).
This approach efficiently handles the problem of maximizing fruit collection while adhering to movement constraints, providing a clear and effective solution.
"""