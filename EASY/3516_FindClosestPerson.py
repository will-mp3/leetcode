"""
You are given three integers x, y, and z, representing the positions of three people on a number line:

x is the position of Person 1.
y is the position of Person 2.
z is the position of Person 3, who does not move.
Both Person 1 and Person 2 move toward Person 3 at the same speed.

Determine which person reaches Person 3 first:

Return 1 if Person 1 arrives first.
Return 2 if Person 2 arrives first.
Return 0 if both arrive at the same time.
Return the result accordingly.
"""

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xd, yd = abs(z - x), abs(z - y)
        if xd == yd:
            return 0
        else:
            return 1 if xd < yd else 2

"""
This code defines a solution to determine which of two people, located at positions x and y on a number line, will reach a third person located at position z first, given that both move towards z at the same speed.
The `findClosest` method calculates the absolute distances from Person 1 (at position x) and Person 2 (at position y) to Person 3 (at position z) using the `abs` function.
It then compares these distances:
- If the distances are equal, it returns 0, indicating that both persons will arrive at the same time.
- If Person 1's distance is less than Person 2's distance, it returns 1, indicating that Person 1 will arrive first.
- Otherwise, it returns 2, indicating that Person 2 will arrive first.
The time complexity of this solution is O(1), as it involves a constant number of arithmetic operations and comparisons. The space complexity is also O(1) since it uses a fixed amount of additional space.
"""