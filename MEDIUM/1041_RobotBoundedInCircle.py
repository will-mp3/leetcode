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
this problem can be solved without the use of any fancy algorithms.
we must start by first understanding what the conditions to return true are.
to determine a cycle we have two conditions:
if after the given instructions the position remains the same (0, 0) then we know that the robot is stuck in a loop.
similarly, if at any point the direction changes from north facing, we know that the robot will also get stuck in a cycle.
to deduce this we define direction coordinates and location coordinates.
we start our robot at (0,0) and point it facing north (0, 1).
we then read through our directions, when we encounter go we move our position based on the current direction coordinates.
when left or right is given, we rotate the direction coordinates by swapping x and y directions and using sign swaps.
the above is difficult to explaina in writing, if confused draw it out.
once the directions have been read we simply check our two conditions mentioned prior and return the result.
"""