"""
You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

We define the right direction as positive x-axis (increasing x-coordinate) and the left direction as negative x-axis (decreasing x-coordinate). 
Similarly, we define the up direction as positive y-axis (increasing y-coordinate) and the down direction as negative y-axis (decreasing y-coordinate)

You have to place n people, including Alice and Bob, at these points such that there is exactly one person at every point. 
Alice wants to be alone with Bob, so Alice will build a rectangular fence with Alice's position as the upper left corner and Bob's position as the lower right corner of the fence (Note that the fence might not enclose any area, i.e. it can be a line). 
If any person other than Alice and Bob is either inside the fence or on the fence, Alice will be sad.

Return the number of pairs of points where you can place Alice and Bob, such that Alice does not become sad on building the fence.

Note that Alice can only build a fence with Alice's position as the upper left corner, and Bob's position as the lower right corner. 
For example, Alice cannot build either of the fences in the picture below with four corners (1, 1), (1, 3), (3, 1), and (3, 3), because:

With Alice at (3, 3) and Bob at (1, 1), Alice's position is not the upper left corner and Bob's position is not the lower right corner of the fence.
With Alice at (1, 3) and Bob at (1, 1), Bob's position is not the lower right corner of the fence.
"""

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # sort by x descending, then y ascending
        points.sort(key=lambda p: (-p[0], p[1]))
        n = len(points)
        res = 0

        for i in range(n - 1):
            minY = float('inf') 
            for j in range(i + 1, n):
                # points[i] is upper-left of points[j]
                if minY > points[j][1] >= points[i][1]:
                    res += 1
                    minY = points[j][1]
        return res

"""
This code defines a solution to count the number of pairs of points (A, B) in a 2D plane such that A is on the upper left side of B and there are no other points in the rectangle formed by A and B.
The `numberOfPairs` method first sorts the list of points in descending order by their x-coordinates and in ascending order by their y-coordinates. This sorting ensures that when iterating through the points, we can efficiently check the conditions for the pairs.
It initializes a variable `res` to keep track of the count of valid pairs. The outer loop iterates through each point as point A, and the inner loop iterates through the subsequent points as point B.
For each pair of points, it checks if point B is on the lower right side of point A (i.e., B's y-coordinate is greater than or equal to A's y-coordinate and less than the minimum y-coordinate seen so far). 
If this condition is met, it increments the count `res` and updates the minimum y-coordinate seen.
Finally, it returns the total count of valid pairs.
The time complexity of this solution is O(n^2), where n is the number of points, due to the nested loops. The space complexity is O(1) as it uses a constant amount of additional space.
"""