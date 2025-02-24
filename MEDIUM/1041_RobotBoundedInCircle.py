"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY = 0, 1
        x, y = 0, 0
        
        for d in instructions:
            if d == "G":
                x, y = x + dirX, y + dirY       
            elif d =="L":
                dirX, dirY = -1*dirY, dirX
            else: # d == "R"
                dirX, dirY = dirY, -1*dirX
        
        # return true if position did not change OR the direction changed from the original
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)

"""

"""